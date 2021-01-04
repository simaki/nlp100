from collections import Counter

import torch
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
import torchtext.experimental.transforms as transforms
import torchtext.experimental.vocab as vocab

from path import project_path
from q70 import NewsDataset
from q73 import ClassifierModule


class EmbeddingTransformer:
    """
    https://towardsdatascience.com/taming-lstms-variable-sized-mini-batches-and-why-pytorch-is-good-for-your-health-61d35642972e

    Parameters
    ----------
    - embedding_dim : int, default 10
        Size of each embedding vector
    - tokenizer : callable
        Tokenizer function.
    - min_freq : int, default 1
        Minimum frequency needed to include a token in the vocabulary.
    - padding_idx : int or None, default 0
        If given, pads the output with the embedding vector at padding_idx
        (initialized to zeros) whenever it encounters the index.
    - max_len : int or None, default 10
        If None, do not truncate.
    """

    def __init__(
        self,
        embedding_dim=10,
        tokenizer=transforms.BasicEnglishNormalize(),
        min_freq=1,
        padding_idx=0,
        max_len=10,
    ):
        self.embedding_dim = embedding_dim
        self.tokenizer = tokenizer
        self.min_freq = min_freq
        self.padding_idx = padding_idx
        self.max_len = max_len

    def fit(self, X):
        """
        Parameters
        ----------
        - X : List[str], len n_documents
            List of documents.
        """
        tokens = self.tokenizer(" ".join(X))
        vocabulary = vocab.Vocab(Counter(tokens), min_freq=self.min_freq)
        vocabulary.insert_token("<PAD>", len(vocabulary))  # Padding token

        self._emb = torch.nn.Embedding(
            num_embeddings=len(vocabulary) + 1,
            embedding_dim=self.embedding_dim,
            padding_idx=self.padding_idx,
        )
        self.stoi_ = {s: i + 1 for s, i in vocabulary.get_stoi().items()}
        self.embeddings_ = self._emb.weight

        return self

    def _doc_to_indices(self, doc):
        """
        doc : str

        indices : shape (n_tokens,)
        """
        tokens = self.tokenizer(doc)
        indices = [self.stoi_.get(token, self.padding_idx) for token in tokens]

        if self.max_len is not None:
            indices = indices[:self.max_len or len(indices)]

        return torch.LongTensor(indices)

    def transform(self, X, y=None):
        """
        Parameters
        ----------
        - X : List[str], len n_documents
            List of documents.

        Returns
        -------
        embedded : Tensor, shape (n_documents, max_n_tokens, vector_size)
        """
        embedded = pad_sequence(
            [self._emb(self._doc_to_indices(doc)) for doc in X], batch_first=True
        )
        return embedded

    def fit_transform(self, X):
        return self.fit(X).transform(X)


class RNNClassifier(torch.nn.Module, ClassifierModule):
    """
    RNN Classifier.

    Parameters
    ----------
    - input_size
    - hidden_size
    - output_size
    """

    def __init__(self, input_size, hidden_size, output_size, nonlinearity="relu"):
        super().__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.nonlinearity = nonlinearity

        self.rnn = torch.nn.RNN(
            input_size=self.input_size,
            hidden_size=self.hidden_size,
            nonlinearity=self.nonlinearity,
            batch_first=True,
        )
        self.output_layer = torch.nn.Linear(self.hidden_size, self.output_size)
        self.softmax = torch.nn.Softmax(1)

    def forward(self, x):
        """
        Parameters
        ----------
        - x : Tensor, shape (n_batch, seq_len, input_size)
            where x0, x1, ... : Tensor, shape (batch, input_size)
        """
        _, x = self.rnn(x)
        x = torch.squeeze(x)
        x = self.output_layer(x)
        x = self.softmax(x)
        return x


if __name__ == "__main__":
    print("\rSolving Q80 ... ", end="")

    torch.manual_seed(42)

    embedding_dim = 3
    hidden_size = 5
    output_size = 4

    # Load
    transformer_X = EmbeddingTransformer(embedding_dim=embedding_dim, min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)

    # Build RNNClassifier
    clf = RNNClassifier(embedding_dim, hidden_size, output_size)

    # Forward
    X_tr, _ = next(iter(DataLoader(data_tr, batch_size=100)))
    print(X_tr.shape)
    y_pred = clf(X_tr)
    x = clf(X_tr)

    print(x)

    print("Done.")

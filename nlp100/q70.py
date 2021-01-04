from collections import Counter

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
import torchtext.experimental.transforms as transforms
import torchtext.experimental.vocab as vocab
from sklearn.preprocessing import LabelEncoder

from path import project_path
from q60 import load_w2v


class _NewsDatasetAll(torch.utils.data.Dataset):
    data_path = project_path / "output/news/data.txt"

    def __init__(self, transformer_X, transformer_y):
        self.transformer_X = transformer_X
        self.transformer_y = transformer_y

        data = pd.read_csv(self.data_path, sep="\t", index_col=0)
        self.X = list(data.TITLE)
        self.y = list(data.CATEGORY)

        if self.transformer_X is not None:
            self.X = self.transformer_X.fit_transform(self.X)
        if self.transformer_y is not None:
            self.y = self.transformer_y.fit_transform(self.y)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]


class NewsDataset(torch.utils.data.Subset):
    """
    Defines news datasets.

    Parameters
    ----------
    - stage : {"tr", "va", "te", None}
    - transformer_X : Transformer
    """

    def __init__(self, stage, transformer_X=None, transformer_y=LabelEncoder()):
        dataset_all = _NewsDatasetAll(
            transformer_X=transformer_X, transformer_y=transformer_y
        )
        n = len(dataset_all)

        if stage == "tr":
            indices = range(int(0.0 * n), int(0.8 * n))
        if stage == "va":
            indices = range(int(0.8 * n), int(0.9 * n))
        if stage == "te":
            indices = range(int(0.9 * n), int(1.0 * n))
        if stage is None:
            indices = range(int(0.0 * n), int(1.0 * n))

        super().__init__(dataset_all, indices)


class _W2VTransformer:
    """
    Word2Vec transformer.

    Parameters
    ----------
    - w2v : gensim.models.KeyedVectors
    - min_freq : int, default 1

    Attributes
    ----------
    - stoi_ : dict[str, int]
        Dictionary from word to index.
    - embeddings_ : torch.Tensor
        FloatTensor containing weights for the Embedding.
    - min_freq : int, default 1
        The minimum frequency needed to include a token in the vocabulary.
    """

    def __init__(self, min_freq=1, root=project_path / "data/news/"):
        w2v = load_w2v()
        self.w2v = w2v
        self.min_freq = min_freq
        self.root = root
        self.padding_idx = 0

    @property
    def embedding(self):
        return torch.nn.Embedding.from_pretrained(
            self.embeddings_, padding_idx=self.padding_idx
        )

    def fit(self, X, y=None, init=False):
        """
        Parameters
        ----------
        - X : List[str]
            List of tokens.
        """
        path_stoi_ = self.root / "w2v_stoi_.txt"
        path_embeddings_ = self.root / "w2v_embeddings_.txt"

        if init or not (path_stoi_.exists() and path_embeddings_.exists()):
            vocabulary = vocab.Vocab(Counter(X), min_freq=self.min_freq)

            vecs = [np.zeros((self.w2v.vector_size,))]  # padding index
            vecs += [
                (
                    self.w2v[w]
                    if w in self.w2v.vocab
                    else np.zeros((self.w2v.vector_size,))
                )
                for w in vocabulary.get_itos()
            ]
            for v in vecs:
                v.flags.writeable = True
            stoi = {s: i + 1 for s, i in vocabulary.get_stoi().items()}
            embeddings = torch.cat([torch.tensor(v).reshape(1, -1) for v in vecs], 0)

            with open(path_stoi_, "w") as f:
                f.write("\n".join("{} {}".format(s, i) for s, i in stoi.items()))
            np.savetxt(path_embeddings_, embeddings)
        else:
            with open(path_stoi_) as f:
                stoi = {line.split()[0]: int(line.split()[1]) for line in f.readlines()}
            embeddings = torch.from_numpy(np.loadtxt(path_embeddings_))

        self.stoi_ = stoi
        self.embeddings_ = embeddings

        return self

    def transform(self, X, y=None):
        """
        Parameters
        ----------
        - X : List[str], len n_tokens
            List of tokens

        Returns
        -------
        embedded : Tensor, (n_tokens, vector_size)
        """
        indices = torch.LongTensor(
            [self.stoi_.get(token, self.padding_idx) for token in X]
        )
        return self.embedding(indices)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)


class MW2VTransformer:
    def __init__(self, min_freq=1, tokenizer=transforms.BasicEnglishNormalize()):
        self.w2v_transformer = _W2VTransformer(min_freq=min_freq)
        self.tokenizer = tokenizer

    def fit(self, X, y=None):
        """
        Parameters
        ----------
        - X : List[str]
            List of documents.
        """
        tokens = self.tokenizer(" ".join(X))
        self.w2v_transformer.fit(tokens)
        return self

    def transform(self, X, y=None):
        """
        Parameters
        ----------
        - X : List[str], len n_documents
            List of documents.

        Returns
        -------
        vec : Tensor, shape (n_documents, vector_size)
        """
        return torch.stack(
            [torch.mean(self.w2v_transformer.transform(doc), 0) for doc in X]
        ).to(dtype=torch.float32)

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)


if __name__ == "__main__":
    print("\rSolving Q70 ... ", end="")

    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)
    data_te = NewsDataset("te", transformer_X)

    def X(data):
        return next(iter(DataLoader(data, batch_size=len(data))))[0]

    def y(data):
        return next(iter(DataLoader(data, batch_size=len(data))))[1]

    np.savetxt(project_path / "data/news/X_tr.txt", X(data_tr))
    np.savetxt(project_path / "data/news/X_va.txt", X(data_va))
    np.savetxt(project_path / "data/news/X_te.txt", X(data_te))
    np.savetxt(project_path / "data/news/y_tr.txt", y(data_tr), fmt="%.0f")
    np.savetxt(project_path / "data/news/y_va.txt", y(data_va), fmt="%.0f")
    np.savetxt(project_path / "data/news/y_te.txt", y(data_te), fmt="%.0f")

    print("Done.")

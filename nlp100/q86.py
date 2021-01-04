from copy import deepcopy

import torch
from torch.utils.data import DataLoader

from path import project_path
from q81 import EmbeddingTransformer
from q70 import NewsDataset
from q73 import ClassifierModule


class CNNClassifier(torch.nn.Module, ClassifierModule):
    """
    CNN Classifier.

    Parameters
    ----------
    - kernel_size : int, default 3
    - stride
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        output_size,
        activator=torch.nn.ReLU(),
    ):
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size

        self.cnn = torch.nn.Conv1d(
            in_channels=self.in_channels,
            out_channels=self.out_channels,
            kernel_size=self.kernel_size,
        )
        self.act = deepcopy(activator)
        self.lin = torch.nn.Linear(out_channels, output_size)
        self.out = torch.nn.Softmax(1)

    def forward(self, x):
        """
        Parameters
        ----------
        - x : Tensor, shape (n_batch, seq_len, input_size)
            where x0, x1, ... : Tensor, shape (batch, input_size)
        """
        x = torch.transpose(x, 1, 2)
        x = self.cnn(x)
        x = self.act(x)
        x = torch.max(x, dim=2).values
        x = self.lin(x)
        x = self.out(x)
        return x


if __name__ == "__main__":

    print("\rSolving Q86 ... ", end="")

    torch.manual_seed(42)

    embedding_dim = 3
    hidden_size = 5
    output_size = 4

    # Load
    transformer_X = EmbeddingTransformer(embedding_dim=embedding_dim, min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)

    # Build CNNClassifier
    clf = CNNClassifier(
        in_channels=embedding_dim,
        out_channels=hidden_size,
        kernel_size=3,
        output_size=4,
    )

    # Forward
    X_tr, _ = next(iter(DataLoader(data_tr, batch_size=2)))
    x = clf(X_tr)

    print(x)

    print("Done.")

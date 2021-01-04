from copy import deepcopy

import torch
import numpy as np
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader

from path import project_path
from q70 import NewsDataset
from q70 import MW2VTransformer


class ClassifierModule:
    """
    Trainable classifier.
    """

    def fit(
        self,
        data,
        validation_data=None,
        optimizer=None,
        criterion=torch.nn.CrossEntropyLoss(),
        n_epochs=100,
        batch_size=None,
        verbose=True,
    ):
        """
        Fit net.

        Parameters
        ----------
        - data : Dataset
        - validation_data : Dataset
        - optimizer : torch.optim.Optimizer or None, default None
            Optimizer.  If None, use SGD.
        - criterion : torch.nn.Module, default torch.nn.CrossEntropyLoss.
            Loss function module.
        - n_epochs :
            Number of epochs.
        - batch_size : int or None, default None
            Number of data in a single batch.
            If None, do not perform batch processing.
        """
        optimizer = optimizer or torch.optim.SGD(self.parameters(), lr=0.1)
        batch_size = batch_size or len(data)

        history = {"loss_tr": [], "acc_tr": []}

        if validation_data:
            history["loss_va"] = []
            history["acc_va"] = []

        for i in range(n_epochs):
            loader = DataLoader(data, batch_size=batch_size, shuffle=True)

            if verbose:
                msg = "\rEpoch {}/{}".format(i + 1, n_epochs)
                print(msg, end="")

            _h = {"loss_tr": [], "acc_tr": []}
            for X, y in loader:
                self.train()

                optimizer.zero_grad()
                y_pred = self(X)
                loss = criterion(y_pred, y)
                loss.backward(retain_graph=True)
                optimizer.step()
                acc = accuracy_score(y, torch.argmax(y_pred, 1).detach().numpy())

                _h["loss_tr"].append(loss.item())
                _h["acc_tr"].append(acc)

            history["loss_tr"].append(np.mean(_h["loss_tr"]).item())
            history["acc_tr"].append(np.mean(_h["acc_tr"]).item())

            if verbose:
                msg = "\r{} loss_tr={:.4e} acc_tr={:.2e}".format(msg, loss, acc)
                print(msg, end="")

            if validation_data:
                self.eval()
                loader = DataLoader(validation_data, batch_size=len(validation_data))
                X, y = next(iter(loader))
                y_pred = self(X)

                loss = criterion(y_pred, y).item()
                acc = accuracy_score(y, torch.argmax(y_pred, 1).detach().numpy())

                history["loss_va"].append(loss)
                history["acc_va"].append(acc)
                if verbose:
                    msg = "\r{} loss_va={:.4e} acc_va={:.2e}".format(msg, loss, acc)
                    print(msg, end="")

            if verbose:
                print("", end="\n")

        return history

    def evaluate(self, data):
        loader = DataLoader(data, batch_size=len(data))
        X, y = next(iter(loader))
        y_pred = self(X)
        acc = accuracy_score(y, torch.argmax(y_pred, 1).detach().numpy())

        return acc


class Net(torch.nn.Module, ClassifierModule):
    """
    Neural network.

    Parameters
    ----------
    - n_features : int or None, default None
        Number of input features.
        If None, determine lazily.
    - n_output : int, default 1
        Number of outputs.
    - n_layers : int, default 4
        Number of hidden layers.
    - n_units : int, default 32
        Number of units in each hidden layer.
    - activation : torch.nn.Module, default torch.nn.ReLU()
        Activation function of hidden layers.
    - out_activation : torch.nn.Module, default torch.nn.Tanh()
        Activation function of output layer.
    - bias : bool, default True
        If false, the layer will not learn an additive bias.
    """

    def __init__(
        self,
        n_features=300,
        n_outputs=4,
        n_layers=1,
        n_units=32,
        activation=torch.nn.ReLU(),
        out_activation=torch.nn.Softmax(1),
        bias=True,
    ):
        super().__init__()

        self.n_features = n_features
        self.n_outputs = n_outputs
        self.n_layers = n_layers
        self.n_units = n_units

        self._layers = torch.nn.ModuleList([])
        self._layers.append(torch.nn.Linear(n_features, n_units, bias=bias))
        self._layers.append(deepcopy(activation))
        for _ in range(n_layers - 1):
            self._layers.append(torch.nn.Linear(n_units, n_units, bias=bias))
            self._layers.append(deepcopy(activation))
        self._layers.append(torch.nn.Linear(n_units, n_outputs, bias=bias))
        self._layers.append(deepcopy(out_activation))

    def forward(self, x):
        for layer in self._layers:
            x = layer(x)
        return x


if __name__ == "__main__":
    print("\rSolving Q73 ... ", end="")

    torch.manual_seed(42)

    # Load dataset
    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    # Build and fit Net
    net = Net(bias=False)
    history = net.fit(data_tr, validation_data=data_va, n_epochs=100, verbose=False)

    # Save
    torch.save(net.state_dict(), project_path / "output/nn/model.pt")
    np.savetxt(project_path / "output/nn/history_loss_tr.txt", history["loss_tr"])
    np.savetxt(project_path / "output/nn/history_loss_va.txt", history["loss_va"])
    np.savetxt(project_path / "output/nn/history_acc_tr.txt", history["acc_tr"])
    np.savetxt(project_path / "output/nn/history_acc_va.txt", history["acc_va"])

    print("Done.")

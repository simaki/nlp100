import torch
import numpy as np

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset


if __name__ == "__main__":
    print("\rSolving Q72 ... ", end="")

    torch.manual_seed(42)

    data_tr = NewsDataset("tr", MW2VTransformer(min_freq=2))
    loader = torch.utils.data.DataLoader(data_tr, batch_size=4)
    X, y = next(iter(loader))

    net = torch.nn.Sequential(torch.nn.Linear(300, 4), torch.nn.Softmax(1))
    criterion = torch.nn.CrossEntropyLoss()

    y_pred = net(X)
    loss = criterion(y_pred, y)
    loss.backward()
    grad = net[0].weight.grad

    np.savetxt(project_path / "output/nn/loss.txt", [loss.detach().numpy()])
    np.savetxt(project_path / "output/nn/grad.txt", grad)

    print("Done.")

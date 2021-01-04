import torch
import numpy as np

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset


if __name__ == "__main__":
    print("\rSolving Q71 ... ", end="")

    torch.manual_seed(42)

    data_tr = NewsDataset("tr", MW2VTransformer(min_freq=2))
    loader0 = torch.utils.data.DataLoader(data_tr)
    loader1 = torch.utils.data.DataLoader(data_tr, batch_size=4)
    X0, y0 = next(iter(loader0))
    X1, y1 = next(iter(loader1))

    net = torch.nn.Sequential(torch.nn.Linear(300, 4), torch.nn.Softmax(1))
    y_pred_0 = net(X0)
    y_pred_1 = net(X1)

    np.savetxt(project_path / "output/nn/y_pred_0.txt", y_pred_0.detach().numpy())
    np.savetxt(project_path / "output/nn/y_pred_1.txt", y_pred_1.detach().numpy())

    print("Done.")

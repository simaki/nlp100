import numpy as np
import torch

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset
from q73 import Net


if __name__ == "__main__":
    print("\rSolving Q74 ... ", end="")

    # Load data and model
    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    net = Net(bias=False)
    net.load_state_dict(torch.load(project_path / "output/nn/model.pt"))

    acc_tr = net.evaluate(data_tr)
    acc_va = net.evaluate(data_va)

    np.savetxt(project_path / "output/nn/acc_tr.txt", [acc_tr])
    np.savetxt(project_path / "output/nn/acc_va.txt", [acc_va])

    print("Done.")

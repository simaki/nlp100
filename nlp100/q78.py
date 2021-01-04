import torch

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset
from q73 import Net


if __name__ == "__main__":
    print("\rSolving Q78 ... ", end="")

    torch.manual_seed(42)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Load dataset
    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    # Build and fit Net
    net = Net().to(device)
    history = net.fit(data_tr, validation_data=data_va)

    print("Done.")

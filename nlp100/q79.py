import torch
import numpy as np

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset
from q73 import Net


if __name__ == "__main__":
    print("\rSolving Q79 ... ", end="")

    torch.manual_seed(42)

    # Load dataset
    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    # Build and fit Net
    net = Net(n_units=32, n_layers=2)
    optimizer = torch.optim.Adam(net.parameters())
    history = net.fit(
        data_tr,
        validation_data=data_va,
        optimizer=optimizer,
        n_epochs=100,
        batch_size=8,
    )

    # Save
    torch.save(net.state_dict(), project_path / "output/nn/model_m.pt")
    np.savetxt(project_path / "output/nn/history_m_loss_tr.txt", history["loss_tr"])
    np.savetxt(project_path / "output/nn/history_m_loss_va.txt", history["loss_va"])
    np.savetxt(project_path / "output/nn/history_m_acc_tr.txt", history["acc_tr"])
    np.savetxt(project_path / "output/nn/history_m_acc_va.txt", history["acc_va"])

    print("Done.")

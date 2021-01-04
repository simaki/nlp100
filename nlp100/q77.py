import torch
import numpy as np
import matplotlib.pyplot as plt

from path import project_path
from q70 import MW2VTransformer
from q70 import NewsDataset
from q73 import Net


if __name__ == "__main__":
    print("\rSolving Q77 ... ", end="")

    torch.manual_seed(42)

    # Load dataset
    transformer_X = MW2VTransformer(min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    # Build and fit Net
    net = Net()
    history = net.fit(data_tr, validation_data=data_va, batch_size=8)

    # Save
    torch.save(net.state_dict(), project_path / "output/nn/model_b.pt")
    np.savetxt(project_path / "output/nn/history_b_loss_tr.txt", history["loss_tr"])
    np.savetxt(project_path / "output/nn/history_b_loss_va.txt", history["loss_va"])
    np.savetxt(project_path / "output/nn/history_b_acc_tr.txt", history["acc_tr"])
    np.savetxt(project_path / "output/nn/history_b_acc_va.txt", history["acc_va"])

    # Plot
    plt.figure()
    plt.plot(history["loss_tr"], label="Loss train")
    plt.plot(history["loss_va"], label="Loss valid")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss")
    plt.savefig(project_path / "output/nn/history_b_loss.png")
    plt.close()

    plt.figure()
    plt.plot(history["acc_tr"], label="Accuracy train")
    plt.plot(history["acc_va"], label="Accuracy valid")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy")
    plt.savefig(project_path / "output/nn/history_b_accuracy.png")
    plt.close()

    print("Done.")

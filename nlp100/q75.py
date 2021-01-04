import numpy as np
import matplotlib.pyplot as plt

from path import project_path


if __name__ == "__main__":
    print("\rSolving Q75 ... ", end="")

    loss_tr = np.loadtxt(project_path / "output/nn/history_loss_tr.txt")
    loss_va = np.loadtxt(project_path / "output/nn/history_loss_va.txt")
    acc_tr = np.loadtxt(project_path / "output/nn/history_acc_tr.txt")
    acc_va = np.loadtxt(project_path / "output/nn/history_acc_va.txt")

    plt.figure()
    plt.plot(loss_tr, label="Loss train")
    plt.plot(loss_va, label="Loss valid")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss")
    plt.savefig(project_path / "output/nn/history_loss.png")
    plt.close()

    plt.figure()
    plt.plot(acc_tr, label="Accuracy train")
    plt.plot(acc_va, label="Accuracy valid")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy")
    plt.savefig(project_path / "output/nn/history_accuracy.png")
    plt.close()

    print("Done.")

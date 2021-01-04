import numpy as np
import scipy
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn

from path import project_path


def score(C, X_tr, y_tr, X_va, y_va):
    lr = LogisticRegression(random_state=42, solver="sag", C=C).fit(X_tr, y_tr)
    acc_tr = lr.score(X_tr, y_tr)
    acc_va = lr.score(X_va, y_va)
    return [acc_tr, acc_va]


if __name__ == "__main__":
    print("\rSolving Q58 ... ", end="")

    # Load
    X_tr = scipy.sparse.load_npz(project_path / "output/news/X_tr.npz")
    X_va = scipy.sparse.load_npz(project_path / "output/news/X_va.npz")
    y_tr = np.loadtxt(project_path / "output/news/y_tr.txt")
    y_va = np.loadtxt(project_path / "output/news/y_va.txt")

    # Score
    array_C = np.linspace(0.1, 5.0, 100)
    array_score = np.array([score(C, X_tr, y_tr, X_va, y_va) for C in array_C])
    array_acc_tr = array_score[:, 0]
    array_acc_va = array_score[:, 1]
    np.savetxt(project_path / "output/news/C.txt", array_C)
    np.savetxt(project_path / "output/news/C_acc_tr.txt", array_acc_tr)
    np.savetxt(project_path / "output/news/C_acc_va.txt", array_acc_va)

    # Plot
    seaborn.set_style("whitegrid")
    plt.figure()
    plt.plot(array_C, array_acc_tr, label="Accuracy train")
    plt.plot(array_C, array_acc_va, label="Accuracy valid")
    plt.title("Logistic Regression")
    plt.xlabel("C")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig(project_path / "output/news/C_acc.png")
    plt.close()

    print("Done.")

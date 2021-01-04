import numpy as np
from sklearn.metrics import confusion_matrix

from path import project_path


if __name__ == "__main__":
    print("\rSolving Q55 ... ", end="")

    y_tr = np.loadtxt(project_path / "output/news/y_tr.txt")
    y_va = np.loadtxt(project_path / "output/news/y_va.txt")
    y_pred_tr = np.loadtxt(project_path / "output/news/y_pred_tr.txt")
    y_pred_va = np.loadtxt(project_path / "output/news/y_pred_va.txt")

    cm_tr = confusion_matrix(y_tr, y_pred_tr)
    cm_va = confusion_matrix(y_va, y_pred_va)

    np.savetxt(project_path / "output/news/cm_tr.txt", cm_tr, fmt="%.0f")
    np.savetxt(project_path / "output/news/cm_va.txt", cm_va, fmt="%.0f")

    print("Done.")

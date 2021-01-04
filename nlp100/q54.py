import numpy as np
import scipy

from path import project_path
from q53 import get_fitted_lr


if __name__ == "__main__":
    print("\rSolving Q54 ... ", end="")

    X_tr = scipy.sparse.load_npz(project_path / "output/news/X_tr.npz")
    X_va = scipy.sparse.load_npz(project_path / "output/news/X_va.npz")
    y_tr = np.loadtxt(project_path / "output/news/y_tr.txt")
    y_va = np.loadtxt(project_path / "output/news/y_va.txt")

    lr = get_fitted_lr()

    y_pred_tr = lr.predict(X_tr)
    y_pred_va = lr.predict(X_va)

    np.savetxt(project_path / "output/news/y_pred_tr.txt", y_pred_tr, fmt="%.0f")
    np.savetxt(project_path / "output/news/y_pred_va.txt", y_pred_va, fmt="%.0f")

    score_tr = lr.score(X_tr, y_tr)
    score_va = lr.score(X_va, y_va)

    np.savetxt(project_path / "output/news/score_tr.txt", [score_tr])
    np.savetxt(project_path / "output/news/score_va.txt", [score_va])

    print("Done.")

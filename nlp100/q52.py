import numpy as np
import scipy
from sklearn.linear_model import LogisticRegression

from path import project_path

names = [
    "ID",
    "TITLE",
    "URL",
    "PUBLISHER",
    "CATEGORY",
    "STORY",
    "HOSTNAME",
    "TIMESTAMP",
]


if __name__ == "__main__":
    print("\rSolving Q52 ... ", end="")

    X_tr = scipy.sparse.load_npz(project_path / "output/news/X_tr.npz")
    y_tr = np.loadtxt(project_path / "output/news/y_tr.txt", dtype=np.int64)
    lr = LogisticRegression(random_state=42, solver="sag").fit(X_tr, y_tr)

    np.savetxt(project_path / "output/news/lr_coef.txt", lr.coef_)
    np.savetxt(project_path / "output/news/lr_intercept.txt", lr.intercept_)
    np.savetxt(project_path / "output/news/lr_classes.txt", lr.classes_, fmt="%.0f")

    print("Done.")

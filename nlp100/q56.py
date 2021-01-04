import os
import pathlib

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    print("\rSolving Q56 ... ", end="")

    # Load
    y_tr = np.loadtxt(project_path / "output/news/y_tr.txt")
    y_va = np.loadtxt(project_path / "output/news/y_va.txt")
    y_pred_tr = np.loadtxt(project_path / "output/news/y_pred_tr.txt")
    y_pred_va = np.loadtxt(project_path / "output/news/y_pred_va.txt")

    # Score
    acc_tr = accuracy_score(y_tr, y_pred_tr)
    acc_va = accuracy_score(y_va, y_pred_va)
    rec_micro_tr = recall_score(y_tr, y_pred_tr, average="micro")
    rec_micro_va = recall_score(y_va, y_pred_va, average="micro")
    rec_macro_tr = recall_score(y_tr, y_pred_tr, average="macro")
    rec_macro_va = recall_score(y_va, y_pred_va, average="macro")
    f1_micro_tr = f1_score(y_tr, y_pred_tr, average="micro")
    f1_micro_va = f1_score(y_va, y_pred_va, average="micro")
    f1_macro_tr = f1_score(y_tr, y_pred_tr, average="macro")
    f1_macro_va = f1_score(y_va, y_pred_va, average="macro")

    # Save
    np.savetxt(project_path / "output/news/score_acc_tr.txt", [acc_tr])
    np.savetxt(project_path / "output/news/score_acc_va.txt", [acc_va])
    np.savetxt(project_path / "output/news/score_rec_micro_tr.txt", [rec_micro_tr])
    np.savetxt(project_path / "output/news/score_rec_micro_va.txt", [rec_micro_va])
    np.savetxt(project_path / "output/news/score_rec_macro_tr.txt", [rec_macro_tr])
    np.savetxt(project_path / "output/news/score_rec_macro_va.txt", [rec_macro_va])
    np.savetxt(project_path / "output/news/score_f1_micro_tr.txt", [f1_micro_tr])
    np.savetxt(project_path / "output/news/score_f1_micro_va.txt", [f1_micro_va])
    np.savetxt(project_path / "output/news/score_f1_macro_tr.txt", [f1_macro_tr])
    np.savetxt(project_path / "output/news/score_f1_macro_va.txt", [f1_macro_va])

    print("Done.")

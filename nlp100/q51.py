import numpy as np
import pandas as pd
import scipy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

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
    print("\rSolving Q51 ... ", end="")

    # Load data
    i_tr = project_path / "data/news/data_tr.txt"
    i_va = project_path / "data/news/data_va.txt"
    i_te = project_path / "data/news/data_te.txt"
    data_tr = pd.read_csv(i_tr, sep="\t", index_col=0)
    data_va = pd.read_csv(i_va, sep="\t", index_col=0)
    data_te = pd.read_csv(i_te, sep="\t", index_col=0)

    # Fit tfidf Transformer
    tv = TfidfVectorizer().fit(data_tr.TITLE)
    with open(project_path / "output/news/tv_vocabulary_.txt", "w") as f:
        f.write("\n".join("{} {}".format(k, v) for k, v in tv.vocabulary_.items()))
    with open(project_path / "output/news/tv_stop_words_.txt", "w") as f:
        f.write("\n".join(tv.stop_words_))
    with open(project_path / "output/news/tv_feature_names.txt", "w") as f:
        f.write("\n".join(tv.get_feature_names()))
    np.savetxt(project_path / "output/news/tv_idf_.txt", tv.idf_)

    # Transform
    X_tr = tv.transform(data_tr.TITLE)
    X_va = tv.transform(data_va.TITLE)
    X_te = tv.transform(data_te.TITLE)
    scipy.sparse.save_npz(project_path / "output/news/X_tr.npz", X_tr)
    scipy.sparse.save_npz(project_path / "output/news/X_va.npz", X_va)
    scipy.sparse.save_npz(project_path / "output/news/X_te.npz", X_te)

    # Encode labels
    le = LabelEncoder().fit(data_tr.CATEGORY)
    with open(project_path / "output/news/le_classes_.txt", "w") as f:
        f.write("\n".join(le.classes_))
    y_tr = le.transform(data_tr.CATEGORY)
    y_va = le.transform(data_va.CATEGORY)
    y_te = le.transform(data_te.CATEGORY)
    np.savetxt(project_path / "output/news/y_tr.txt", y_tr, fmt="%.0f")
    np.savetxt(project_path / "output/news/y_va.txt", y_va, fmt="%.0f")
    np.savetxt(project_path / "output/news/y_te.txt", y_te, fmt="%.0f")

    print("Done.")

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
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


def get_fitted_tv():
    with open(project_path / "output/news/tv_vocabulary_.txt") as f:
        vocabulary_ = {line.split()[0]: int(line.split()[1]) for line in f.readlines()}
    with open(project_path / "output/news/tv_stop_words_.txt") as f:
        stop_words_ = list(f.readlines())
    idf_ = np.loadtxt(project_path / "output/news/tv_idf_.txt")

    tv = TfidfVectorizer(stop_words=stop_words_, vocabulary=vocabulary_)
    tv.idf_ = idf_

    return tv


def get_fitted_lr():
    coef_ = np.loadtxt(project_path / "output/news/lr_coef.txt")
    intercept_ = np.loadtxt(project_path / "output/news/lr_intercept.txt")
    classes_ = np.loadtxt(project_path / "output/news/lr_classes.txt")

    lr = LogisticRegression()
    lr.coef_, lr.intercept_, lr.classes_ = coef_, intercept_, classes_

    return lr


def predict(raw_documents):
    tv = get_fitted_tv()
    lr = get_fitted_lr()

    X = tv.transform(raw_documents)
    y = lr.predict(X)

    return y


if __name__ == "__main__":
    print("\rSolving Q53 ... ", end="")

    i_tr = project_path / "data/news/data_tr.txt"
    i_va = project_path / "data/news/data_va.txt"
    data_tr = pd.read_csv(i_va, sep="\t", index_col=0)
    data_va = pd.read_csv(i_va, sep="\t", index_col=0)

    y_pred_tr = predict(data_tr.TITLE)
    y_pred_va = predict(data_va.TITLE)
    np.savetxt(project_path / "output/news/y_pred_tr.txt", y_pred_tr, fmt="%.0f")
    np.savetxt(project_path / "output/news/y_pred_va.txt", y_pred_va, fmt="%.0f")

    print("Done.")

import numpy as np
import optuna
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from path import project_path


data_tr = pd.read_csv(project_path / "data/news/data_tr.txt", sep="\t", index_col=0)
data_va = pd.read_csv(project_path / "data/news/data_va.txt", sep="\t", index_col=0)
y_tr = np.loadtxt(project_path / "data/news/y_tr.txt")
y_va = np.loadtxt(project_path / "data/news/y_va.txt")


def objective(trial):
    # Feature extraction
    fe_name = trial.suggest_categorical("fe", ["CountVectorizer", "TfidfVectorizer"])
    cv_stop_words = trial.suggest_categorical("cv_stop_words", [None, "english"])
    if fe_name == "CountVectorizer":
        fe = CountVectorizer(stop_words=cv_stop_words)
    if fe_name == "TfidfVectorizer":
        fe = TfidfVectorizer(stop_words=cv_stop_words)

    # Class
    cl_name = trial.suggest_categorical("cl", ["LogisticRegression", "RandomForest"])

    if cl_name == "LogisticRegression":
        C = trial.suggest_loguniform("lr_C", 0.1, 20.0)
        cl = LogisticRegression(C=C, solver="sag", random_state=42, max_iter=1000)
    if cl_name == "RandomForest":
        max_depth = trial.suggest_int("rf_max_depth", 2, 32)
        cl = RandomForestClassifier(max_depth=max_depth, random_state=42)

    # Score
    pipeline = Pipeline([("fe", fe), ("cl", cl)]).fit(data_tr.TITLE, y_tr)
    accuracy = pipeline.score(data_va.TITLE, y_va)

    return accuracy


if __name__ == "__main__":
    print("\rSolving Q59 ... ", end="")

    optuna.logging.set_verbosity(0)

    # Optimize
    sampler = optuna.samplers.RandomSampler(seed=42)
    study = optuna.create_study(sampler=sampler, direction="maximize")
    study.optimize(objective, n_trials=100)

    # Save
    with open(project_path / "output/news/opt_best_params.txt", "w") as f:
        f.write("\n".join("{}: {}".format(k, v) for k, v in study.best_params.items()))
    np.savetxt(project_path / "output/news/opt_best_accuracy.txt", [study.best_value])
    trials_dataframe = study.trials_dataframe(attrs=["value", "params"])
    trials_dataframe.to_csv(project_path / "output/news/opt_trials.csv")

    print("Done.")

import pandas as pd
from tqdm import tqdm

from path import project_path
from q60 import load_w2v
from q63 import analogy


def load_question_words():
    data = pd.read_csv(
        project_path / "data/w2v/questions-words.txt", sep=" ", skiprows=1, header=None,
    )
    data = data[data.iloc[:, 0] != ":"]
    return data


if __name__ == "__main__":
    print("\rSolving Q64 ... ", end="")

    w2v = load_w2v()

    data = load_question_words()
    analogies = [
        analogy(w2v, r[1], r[0], r[2], topn=1)[0]
        for _, r in tqdm(list(data.iterrows()))
    ]
    data.insert(4, 4, [a[0] for a in analogies])
    data.insert(5, 5, [a[1] for a in analogies])

    data.to_csv(project_path / "output/w2v/analogy.csv")

    print("Done.")

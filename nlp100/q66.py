import pandas as pd
import numpy as np
import scipy
from sklearn.metrics.pairwise import cosine_similarity

from path import project_path
from q60 import load_w2v


if __name__ == "__main__":
    w2v = load_w2v()

    def cos(w0, w1):
        return cosine_similarity(w2v[w0].reshape(1, -1), w2v[w1].reshape(1, -1))[0][0]

    data = pd.read_csv(project_path / "data/w2v/wordsim353/combined.csv")
    data["cos"] = [cos(row["Word 1"], row["Word 2"]) for _, row in data.iterrows()]
    r, _ = scipy.stats.spearmanr(data["Human (mean)"], data["cos"])

    data.to_csv(project_path / "output/w2v/wordsim.csv")
    np.savetxt(project_path / "output/w2v/wordsim-spearmanr.txt", [r])

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from path import project_path


if __name__ == "__main__":
    print("\rSolving Q61 ... ", end="")

    v0 = np.loadtxt(project_path / "output/w2v/v_united_states.txt").reshape(1, -1)
    v1 = np.loadtxt(project_path / "output/w2v/v_us.txt").reshape(1, -1)
    cos = cosine_similarity(v0, v1)

    np.savetxt(project_path / "output/w2v/cos_us.txt", cos)

    print("Done.")

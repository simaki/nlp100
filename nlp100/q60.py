import numpy as np
import gensim

from path import project_path


def load_w2v(path=project_path / "data/w2v/GoogleNews-vectors-negative300.bin"):
    return gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)


if __name__ == "__main__":
    print("\rSolving Q60 ... ", end="")

    w2v = load_w2v()
    v0 = w2v["United_States"]
    v1 = w2v["U.S."]

    np.savetxt(project_path / "output/w2v/v_united_states.txt", v0)
    np.savetxt(project_path / "output/w2v/v_us.txt", v1)

    print("Done.")

from path import project_path
from q60 import load_w2v


def analogy(w2v, w0, w1, w2, **kwargs):
    """
    Return analogy `w0 - w1 + w2`.
    """
    return w2v.most_similar(positive=[w2v[w0], w2v[w2]], negative=[w2v[w1]], **kwargs)


if __name__ == "__main__":
    print("\rSolving Q63 ... ", end="")

    w2v = load_w2v()
    s = analogy(w2v, "Spain", "Madrid", "Athens")

    with open(project_path / "output/w2v/similar_spain.txt", "w") as f:
        f.write("\n".join("{} {}".format(*w) for w in s))

    print("Done.")

from path import project_path

from q60 import load_w2v


if __name__ == "__main__":
    print("\rSolving Q62 ... ", end="")

    w2v = load_w2v()
    v = w2v["United_States"]
    s = w2v.most_similar(positive=[v])

    with open(project_path / "output/w2v/similar_us.txt", "w") as f:
        f.write("\n".join("{} {}".format(*w) for w in s[:10]))

    print("Done.")

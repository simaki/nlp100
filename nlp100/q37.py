import os
import pathlib

import matplotlib.pyplot as plt
import seaborn

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


def neko(sentence):
    return any(w["base"] == "猫" for w in sentence)


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    output_txt = project_path / "output/q37_neko_withneko.txt"
    output_png = project_path / "output/q37_neko_withneko.png"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    words_with_neko = []
    for sentence in sentences:
        if neko(sentence):
            words_with_neko += [w["base"] for w in sentence]

    occ = {}
    for w in words_with_neko:
        occ[w] = occ.get(w, 0) + 1

    frequent_words = [(n, w) for w, n in occ.items()]
    frequent_words = sorted(frequent_words, reverse=True)

    with open(output_txt, "w") as f:
        for i in frequent_words:
            f.write("{} {}".format(*i))
            f.write("\n")

    n = [n for n, w in frequent_words[:100]]

    seaborn.set_style("whitegrid")
    plt.figure()
    plt.bar(range(100), n)
    plt.savefig(output_png)
    plt.close()

import os
import pathlib

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    output = project_path / "output/q35_neko_occ.txt"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    occ = {}
    for sentence in sentences:
        for word in sentence:
            occ[word["base"]] = occ.get(word["base"], 0) + 1

    frequent_words = [(n, w) for w, n in occ.items()]
    frequent_words = sorted(frequent_words, reverse=True)

    with open(output, "w") as f:
        for i in frequent_words:
            f.write("{} {}".format(*i))
            f.write("\n")

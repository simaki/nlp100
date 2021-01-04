import os
import pathlib

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    output = project_path / "output/q34_neko_succ_noun.txt"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    list_succ_nouns = []
    for sentence in sentences:
        nouns = []
        for w in sentence:
            if w["pos"] == "名詞":
                nouns.append(w["surface"])
            else:
                if len(nouns) > 1:
                    list_succ_nouns.append(nouns)
                nouns = []
        if len(nouns) > 1:
            list_succ_nouns.append(nouns)

    with open(output, "w") as f:
        for nouns in list_succ_nouns:
            f.write(",".join(nouns))
            f.write("\n")

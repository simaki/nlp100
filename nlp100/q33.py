import os
import pathlib

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    neko_anob = project_path / "output/q33_neko_verbs_anob.txt"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    list_anob = []
    for sentence in sentences:
        for w0, w1, w2 in zip(sentence, sentence[1:], sentence[2:]):
            if w1["base"] == "の":
                anob = w0["surface"] + w1["surface"] + w2["surface"]
                list_anob.append(anob)

    with open(neko_anob, "w") as f:
        for anob in list_anob:
            f.write(anob)
            f.write("\n")

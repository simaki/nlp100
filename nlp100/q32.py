import os
import pathlib

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    neko_verbs_base = project_path / "output/q32_neko_verbs_base.txt"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    verbs = set()
    for sentence in sentences:
        for word in sentence:
            if word["pos"] == "動詞":
                verbs.add(word["base"])

    with open(neko_verbs_base, "w") as f:
        for verb in verbs:
            f.write(verb)
            f.write("\n")

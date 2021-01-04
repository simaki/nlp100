import os
import pathlib

from q30 import read

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    neko_verbs_surface = project_path / "output/q31_neko_verbs_surface.txt"

    with open(neko_mecab) as f:
        s = f.read()
        sentences = read(s)

    verbs = set()
    for sentence in sentences:
        for word in sentence:
            if word["pos"] == "動詞":
                verbs.add(word["surface"])

    with open(neko_verbs_surface, "w") as f:
        for verb in verbs:
            f.write(verb)
            f.write("\n")

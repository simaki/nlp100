import os
import pathlib

import MeCab as mecab

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


def parse(s):
    m = mecab.Tagger("-d /usr/local/lib/mecab/dic/ipadic -Ochasen")
    return m.parse(s)


def read(mecab_string):
    sentences = []
    sentence = []

    for line in mecab_string.split("\n"):
        if line == "EOS":
            break
        features = line.split("\t")
        features = features[:3] + features[3].split("-") + [""]
        word = dict(zip(["surface", "yomi", "base", "pos", "pos1"], features))

        if word["surface"] in ("\u3000",):
            continue

        sentence.append(word)

        if word["surface"] == "。":
            sentences.append(sentence)
            sentence = []

    return sentences


if __name__ == "__main__":
    neko = project_path / "data/neko.txt"
    neko_mecab = project_path / "data/neko.txt.mecab"

    with open(neko) as f:
        s = f.read()

    w = parse(s)

    with open(neko_mecab, "w") as f:
        f.write(w)

    with open(neko_mecab) as f:
        s = f.read()

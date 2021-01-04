import os
import pathlib

import matplotlib.pyplot as plt
import seaborn

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    neko_mecab = project_path / "data/neko.txt.mecab"
    neko_occ = project_path / "output/q35_neko_occ.txt"
    output = project_path / "output/q30_neko_occ.png"

    with open(neko_occ) as f:
        ns = [int(line.split(" ")[0]) for line in f.readlines()]

    occ = [0 for _ in range(ns[0])]

    for n in ns:
        occ[n - 1] += 1

    seaborn.set_style("whitegrid")
    plt.figure()
    plt.plot(range(1, ns[0] + 1), occ)
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig(output)
    plt.close()

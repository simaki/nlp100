import os
import pathlib

import matplotlib.pyplot as plt
import seaborn

project_path = pathlib.Path(os.path.dirname(__file__)) / ".."


if __name__ == "__main__":
    occ = project_path / "output/q35_neko_occ.txt"
    output = project_path / "output/q36_occ.png"

    with open(occ) as f:
        s = f.read()

    n = [int(i.split(" ")[0]) for i in s.split("\n")[:100]]

    seaborn.set_style("whitegrid")
    plt.figure()
    plt.bar(range(100), n)
    plt.savefig(output)
    plt.close()

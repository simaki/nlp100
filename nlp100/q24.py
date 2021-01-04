import re

from path import project_path
from q21 import load_uk


if __name__ == "__main__":
    print("\rSolving Q24 ... ", end="")

    r = re.findall(r"\[\[ファイル:(.+?)\|", load_uk())

    with open(project_path / "output/wiki/24.txt", "w") as f:
        f.write("\n".join(r))

    print("Done.")

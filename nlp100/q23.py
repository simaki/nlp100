import re

from path import project_path
from q21 import load_uk


if __name__ == "__main__":
    print("\rSolving Q23 ... ", end="")

    r = re.findall(r"(={2,})\s?([^=]+)\s?\1", load_uk())

    with open(project_path / "output/wiki/23.txt", "w") as f:
        f.write("\n".join("{} {}".format(len(s[0]), s[1]) for s in r))

    print("Done.")

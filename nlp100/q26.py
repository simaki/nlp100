import re

from path import project_path
from q21 import load_uk
from q25 import read_info
from q25 import info_to_dict


def rm_emph(text):
    return re.sub(r"('{2,})([^']+)\1", r"\2", text)


if __name__ == "__main__":
    print("\rSolving Q26 ... ", end="")

    r = info_to_dict(rm_emph(read_info(load_uk())))

    with open(project_path / "output/wiki/26.txt", "w") as f:
        f.write("\n".join("{} {}".format(k, v) for k, v in r.items()))

    print("Done.")

import re

from path import project_path
from q21 import load_uk
from q25 import read_info
from q25 import info_to_dict
from q26 import rm_emph
from q27 import rm_link


def rm_tags(text):
    text = re.sub(r"<br />", r"", text)
    text = re.sub(r"<([^>\s]+)(\s[^>]+)*(>[^<]*</\1>|\s*/>)", r"", text)
    return text


if __name__ == "__main__":
    print("\rSolving Q28 ... ", end="")

    x = info_to_dict(rm_tags(rm_link(rm_emph(read_info(load_uk())))))

    with open(project_path / "output/wiki/28.txt", "w") as f:
        f.write("\n".join("{} {}".format(k, v) for k, v in x.items()))

    print("Done.")

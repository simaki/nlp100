import re

from path import project_path
from q21 import load_uk
from q25 import read_info
from q25 import info_to_dict
from q26 import rm_emph


def rm_link(text):
    text = re.sub(r"{{Cite[^}]+}}", r"", text)
    text = re.sub(r"{{\d}}", r"", text)
    text = re.sub(r"{{en icon}}", r"", text)
    text = re.sub(r"{{([^}]+\|)*([^}]+)}}", r"\2", text)
    text = re.sub(r"\[\[ファイル:([^\]]+)+\]\]", r"", text)
    text = re.sub(r"\[\[([^\]]+\|)*([^\]]+)\]\]", r"\2", text)
    return text


if __name__ == "__main__":
    print("\rSolving Q27 ... ", end="")

    r = info_to_dict(rm_link(rm_emph(read_info(load_uk()))))

    with open(project_path / "output/wiki/27.txt", "w") as f:
        f.write("\n".join("{} {}".format(k, v) for k, v in r.items()))

    print("Done.")

import re

from path import project_path
from q21 import load_uk


def read_info(text):
    text = text.replace("\n", "")
    return re.findall(r"{{基礎情報 国\|((?:[^{{}}]*{{[^{{}}]*}})*[^{{}}]*)}}", text)[0]


def info_to_dict(info):
    x = info

    r0 = r"({{[^}\|]+)\|([^}]+}})"
    r1 = r"\1<PIPE>\2"
    while x != re.sub(r0, r1, x):
        x = re.sub(r0, r1, x)

    r0 = r"(\[\[[^\]\|]+)\|([^\]]+\]\])"
    r1 = r"\1<PIPE>\2"
    while x != re.sub(r0, r1, x):
        x = re.sub(r0, r1, x)

    items = [i.replace("<PIPE>", "|") for i in re.split(r"\|", x)]

    return dict([re.findall(r"(\S+)\s*=\s*(.+)", item)[0] for item in items])


if __name__ == "__main__":
    print("\rSolving Q25 ... ", end="")

    r = info_to_dict(read_info(load_uk()))

    with open(project_path / "output/wiki/25.txt", "w") as f:
        f.write("\n".join("{} {}".format(k, v) for k, v in r.items()))

    print("Done.")

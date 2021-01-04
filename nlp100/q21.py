import re

from path import project_path


def load_uk(path=project_path / "data/wiki/uk.txt"):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    print("\rSolving Q21 ... ", end="")

    r = re.findall(r"\[\[Category:.*\]\]", load_uk())

    with open(project_path / "output/wiki/21.txt", "w") as f:
        f.write("\n".join(r))

    print("Done.")

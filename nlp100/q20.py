import json

from path import project_path


def pick_uk(path=project_path / "data/wiki/jawiki-country.json"):
    with open(path) as f:
        for line in f.readlines():
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]


if __name__ == "__main__":
    print("\rSolving Q20 ... ", end="")

    with open(project_path / "data/wiki/uk.txt", "w") as f:
        f.write(pick_uk())

    print("Done.")

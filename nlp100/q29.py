import requests

from path import project_path
from q21 import load_uk
from q25 import read_info
from q25 import info_to_dict


if __name__ == "__main__":
    print("\rSolving Q29 ... ", end="")

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "imageinfo",
        "iiprop": ["url"],
        "format": "json",
        "titles": "File:{}".format(info_to_dict(read_info(load_uk()))["国旗画像"]),
    }
    r = requests.get(url=url, params=params).json()
    r = r["query"]["pages"]["23473560"]["imageinfo"][0]["url"]

    with open(project_path / "output/wiki/29.txt", "w") as f:
        f.write(r)

    print("Done.")

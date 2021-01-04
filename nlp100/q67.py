import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from path import project_path
from q60 import load_w2v


def fetch_countries():
    url = "https://raw.githubusercontent.com/datasets/country-list/master/data.csv"
    countries = [s.split(",")[0].replace(" ", "_") for s in pd.read_csv(url)["Name"]]
    countries = list(set(countries))
    return countries


if __name__ == "__main__":
    print("\rSolving Q67 ... ", end="")

    w2v = load_w2v()

    countries = [s for s in fetch_countries() if s in w2v.vocab]
    X = np.stack([w2v[s] for s in countries], 0)
    labels = KMeans(5, random_state=42).fit_predict(X)

    result = pd.DataFrame({"Name": countries, "Label": labels})
    result = result.sort_values("Label").reset_index(drop=True)

    np.savetxt(project_path / "output/w2v/country_name.txt", countries, fmt="%s")
    np.savetxt(project_path / "output/w2v/country_X.txt", X)
    result.to_csv(
        project_path / "output/w2v/cluster_country.txt",
        sep=" ",
        header=False,
        index=False,
    )

    print("Done.")

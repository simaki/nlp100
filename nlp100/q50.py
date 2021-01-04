import pandas as pd

from path import project_path

names = [
    "ID",
    "TITLE",
    "URL",
    "PUBLISHER",
    "CATEGORY",
    "STORY",
    "HOSTNAME",
    "TIMESTAMP",
]


if __name__ == "__main__":
    print("\rSolving Q50 ... ", end="")

    i = project_path / "data/news/NewsAggregatorDataset/newsCorpora.csv"
    data = pd.read_csv(i, sep="\t", names=names, index_col="ID")

    # Filter publisher
    allowlist_publisher = [
        "Reuters",
        "Huffington Post",
        "Businessweek",
        "Contactmusic.com",
        "Daily Mail",
    ]
    data = data[data.PUBLISHER.isin(allowlist_publisher)]

    # Random sort
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)

    data.to_csv(project_path / "output/news/data.txt", sep="\t")

    # Split train, valid, test
    n = len(data.index)
    data_tr = data[: int(0.8 * n)]
    data_va = data[int(0.8 * n) : int(0.9 * n)]
    data_te = data[int(0.9 * n) :]

    # Save
    data_tr.to_csv(project_path / "data/news/data_tr.txt", sep="\t")
    data_va.to_csv(project_path / "data/news/data_va.txt", sep="\t")
    data_te.to_csv(project_path / "data/news/data_te.txt", sep="\t")

    print("Done.")

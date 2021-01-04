import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

from path import project_path


if __name__ == "__main__":
    c = np.loadtxt(project_path / "output/w2v/country_name.txt", dtype=str)
    X = np.loadtxt(project_path / "output/w2v/country_X.txt")

    X = PCA(n_components=50, random_state=42).fit_transform(X)
    X = TSNE(random_state=42).fit_transform(X)

    n_clusters = 5
    labels = KMeans(n_clusters=n_clusters, random_state=42).fit(X).labels_

    plt.figure(figsize=(12, 12))
    for i in range(n_clusters):
        x = X[(labels == i).nonzero()]
        plt.scatter(x[:, 0], x[:, 1])
    for i, name in enumerate(c):
        plt.text(X[i, 0], X[i, 1], name)
    plt.savefig(project_path / "output/w2v/tsne.png")
    plt.close()

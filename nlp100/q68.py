import matplotlib.pyplot as plt
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering

from path import project_path


def plt_dendrogram(cluster, **kwargs):
    counts = np.zeros(cluster.children_.shape[0])
    n_samples = len(cluster.labels_)
    for i, merge in enumerate(cluster.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    lm = np.column_stack([ac.children_, ac.distances_, counts])
    scipy.cluster.hierarchy.dendrogram(lm, **kwargs)


if __name__ == "__main__":
    print("\rSolving Q68 ... ", end="")

    c = np.loadtxt(project_path / "output/w2v/country_name.txt", dtype=str)
    X = np.loadtxt(project_path / "output/w2v/country_X.txt")

    ac = AgglomerativeClustering(
        compute_full_tree=True, n_clusters=None, distance_threshold=0,
    ).fit(X)

    plt.figure(figsize=(6, 30))
    plt_dendrogram(ac, leaf_label_func=lambda i: c[i], orientation="right")
    plt.savefig(project_path / "output/w2v/dendrogram.png", dpi=300)
    plt.close()

    print("Done.")

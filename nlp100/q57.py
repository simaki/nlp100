import numpy as np

from path import project_path
from q53 import get_fitted_tv
from q53 import get_fitted_lr


if __name__ == "__main__":
    print("\rSolving Q57 ... ", end="")

    # Load
    tv = get_fitted_tv()
    lr = get_fitted_lr()
    with open(project_path / "output/news/le_classes_.txt") as f:
        classes = np.array(f.read().splitlines())
    with open(project_path / "output/news/tv_feature_names.txt") as f:
        features = np.array(f.read().splitlines())

    # Analyze
    argmax_flatten = np.argsort(lr.coef_, axis=None)[-100:][::-1]
    argmax = np.unravel_index(argmax_flatten, lr.coef_.shape)
    max_w = np.stack([classes[argmax[0]], features[argmax[1]]], axis=-1)

    argmin_flatten = np.argsort(lr.coef_, axis=None)[:100]
    argmin = np.unravel_index(argmin_flatten, lr.coef_.shape)
    min_w = np.stack([classes[argmin[0]], features[argmin[1]]], axis=-1)

    # Save
    np.savetxt(project_path / "output/news/weight_max.txt", max_w, fmt="%s")
    np.savetxt(project_path / "output/news/weight_min.txt", min_w, fmt="%s")

    print("Done.")

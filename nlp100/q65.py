import numpy as np
import pandas as pd

from path import project_path


if __name__ == "__main__":
    print("\rSolving Q65 ... ", end="")

    data = pd.read_csv(project_path / "output/analogy.txt")
    n = len(data.index)
    k = data[data.iloc[:, 3] == data.iloc[:, 4]].sum()

    np.savetxt(project_path / "output/analogy_acc.txt", [k / n])

    print("Done.")

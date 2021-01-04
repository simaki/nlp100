import torch

from path import project_path
from q70 import NewsDataset
from q81 import EmbeddingTransformer
from q86 import CNNClassifier


if __name__ == "__main__":
    print("\rSolving Q82 ... ", end="")

    embedding_dim = 2
    hidden_size = 2
    kernel_size=3
    output_size = 4

    torch.manual_seed(42)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Load
    transformer_X = EmbeddingTransformer(embedding_dim=embedding_dim, min_freq=2)
    data_tr = NewsDataset("tr", transformer_X)
    data_va = NewsDataset("va", transformer_X)

    # Build RNNClassifier
    clf = CNNClassifier(
        in_channels=embedding_dim,
        out_channels=hidden_size,
        kernel_size=kernel_size,
        output_size=output_size,
    ).to(device)
    # clf.fit(data_tr, validation_data=data_va, n_epochs=10, batch_size=16)
    clf.fit(data_tr, validation_data=data_va)

    print("Done.")

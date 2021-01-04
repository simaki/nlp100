from collections import Counter, OrderedDict

from torch.utils.data import DataLoader
import torchtext.experimental.transforms as transforms
import torchtext.experimental.vocab as vocab

from path import project_path
from q70 import NewsDataset


if __name__ == "__main__":
    # Load
    data_tr = NewsDataset("tr")
    docs_tr = next(iter(DataLoader(data_tr, batch_size=len(data_tr))))[0]

    # Tokenize
    tokenizer = transforms.BasicEnglishNormalize()
    tokens = tokenizer(" ".join(docs_tr))

    # Get vocabulary
    common_tokens = OrderedDict(Counter(tokens).most_common())
    vocabulary = vocab.Vocab(common_tokens, min_freq=2)
    stoi = vocabulary.get_stoi()

    # Save
    with open(project_path / "output/rnn/stoi.txt", "w") as f:
        f.write("\n".join("{} {}".format(s, i + 1) for s, i in stoi.items()))

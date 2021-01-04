import numpy as np
import transformers
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertModel
from torch import optim
from torch import cuda
import time
from matplotlib import pyplot as plt

from path import project_path
from q70 import NewsDataset
from q73 import ClassifierModule


class BERTTokenizeTransformer:
    def __init__(self, max_length=10, tokenizer=BertTokenizer()):
        self.max_length = max_length
        self.tokenizer = tokenizer

    def fit(self, X):
        pass

    def _transform_one(self, doc):
        t = self.tokenizer.encode_plus(
            doc,
            add_special_tokens=True,
            max_length=self.max_length,
            pad_to_max_length=True,
        )
        return (t["input_ids"], t["attention_mask"])

    def transform(self, X):
        """
        Parameters
        ----------
        - X : List[str], len n_tokens
            List of docs

        Returns
        -------
        X_transformed : shape (n_documents, max_len, 2)
        """
        t = [self._transform_one(doc) for doc in X]
        x = torch.cat(
            [
                [ti[0] for ti in t],
                [ti[1] for ti in t],
            ],
            1,
        )
        return torch.LongTensor(x)


class BERTClassifier(torch.nn.Module, ClassifierModule):
    """
    ...
    """

    def __init__(self, output_size=4):
        super().__init__()

        self.bert = BertModel("bert-model-uncased")
        self.lin = torch.nn.Linear(768, output_size=4)
        self.out = torch.nn.Softmax(1)

    def forward(self, ids, mask):
        _, x = self.bert(ids, attention_mask=mask)
        x = self.lin(x)
        x = self.out(x)
        return x

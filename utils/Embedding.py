import torch
from torch.nn as nn

class LookUp:
    def __init__(self, vocab_len, embedding_size):
        self.total_words = vocab_len
        self.embed_size = embedding_size
        self.embedding = nn.Embedding(num_embeddings = self.total_words, embedding_dim = self.embed_size)

    def token2embedding(self, tokens):
        token_ids = torch.tensor(tokens)
        token_embeddings = self.embedding(token_id)
        return token_embedding


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

def positionalEncoding(seq_len, embedding_size):
    positions = torch.arange(seq_len, dtype=torch.float32, device=device).unsqueeze(1)
    dims = torch.arange(d_model, dtype=torch.float32, device=device).unsqueeze(0)
    angle_rates = 1 / torch.pow(10000, (2 * (dims // 2)) / d_model)
    
    pe = torch.zeros((seq_len, d_model))
    pe[:, 0::2] = torch.sin(positions * angle_rates[:, 0::2])
    pe[:, 1::2] = torch.cos(positions * angle_rates[:, 1::2])

    return pe

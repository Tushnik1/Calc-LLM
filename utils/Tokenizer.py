import re

class Tokenizer:
    def __init__(self):
        self.word2id = {}
        self.id2word = {}

    def tokenize(self, text):
        text.lower()
        tokens = re.findall(r"\w+|[+\-*/^=<>!]+", text)
        return tokens
    
    def vocab_build(self, texts):

        vocab = set()

        for text in texts:
            tokens = self.tokenize(text)
            vocab.update(tokens)

        vocab = sorted(vocab)
        vocab = ['<UNK>', '<PAD>'] + vocab

        self.word2id = {word:id for id, word in enumerate(vocab)}
        self.id2word = {id:word for word, id in self.word2id.items()}

    def encode(self, text):
        tokens = self.tokenize(text)
        return tokens
    
    def decode(self, tokens):
        words = [self.id2word.get(token, '<UNK>') for token in tokens]
        text = ' '.join(words)
        return text
    
    def vocab_len(self):
        return len(self.word2id)
import math
from collections import Counter

docs = [
    "I'd like an apple.",
    "An apple a day keeps the doctor away.",
    "Never compare an apple to an orange.",
    "I prefer scikit-learn to orange."
]

#STOPWORDS (important)
stopwords = {"a", "an", "the", "to", "i", "d", "like"}

def tokenize(doc):
    words = doc.lower().replace(".", "").replace(",", "").replace("'", "").split()
    return [w for w in words if w not in stopwords]

tokens = [tokenize(doc) for doc in docs]

vocab = sorted(set(word for doc in tokens for word in doc))

def compute_tf(doc):
    tf = Counter(doc)
    total = len(doc)
    return {word: tf[word] / total for word in vocab}

tf_vectors = [compute_tf(doc) for doc in tokens]

# IDF
N = len(docs)
idf = {}
for word in vocab:
    df = sum(1 for doc in tokens if word in doc)
    idf[word] = math.log(N / df)

def compute_tfidf(tf):
    return [tf[word] * idf[word] for word in vocab]

tfidf_vectors = [compute_tfidf(tf) for tf in tf_vectors]

def cosine(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a*a for a in v1))
    norm2 = math.sqrt(sum(b*b for b in v2))
    return dot / (norm1 * norm2)

sims = [cosine(tfidf_vectors[0], tfidf_vectors[i]) for i in range(len(docs))]
sims[0] = -1

print(sims.index(max(sims)) + 1)
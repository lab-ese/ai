import math
from collections import Counter

def get_tokens(text): return text.lower().replace(".", "").replace(",", "").split()

def calculate_similarity(text1, text2):
    w1, w2 = get_tokens(text1), get_tokens(text2)
    v1, v2 = Counter(w1), Counter(w2)
    vocab = set(v1.keys()) | set(v2.keys())
    dot = sum(v1.get(w, 0) * v2.get(w, 0) for w in vocab)
    m1 = math.sqrt(sum(x**2 for x in v1.values()))
    m2 = math.sqrt(sum(x**2 for x in v2.values()))
    cos = dot / (m1 * m2) if m1 and m2 else 0.0
    s1, s2 = set(w1), set(w2)
    jac = len(s1 & s2) / len(s1 | s2) if (s1 | s2) else 0.0
    return cos, jac

if __name__ == "__main__":
    print("--- NLP: TEXT SIMILARITY ---")
    doc1 = input("Sentence 1: ")
    doc2 = input("Sentence 2: ")
    c, j = calculate_similarity(doc1, doc2)
    print(f"Cosine Similarity: {c:.4f}\nJaccard Similarity: {j:.4f}")

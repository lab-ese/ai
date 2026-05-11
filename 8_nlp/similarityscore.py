"""
Similarity Score — Cosine Similarity between two sentences

Run (Windows):
    python similarityscore.py
"""

import re
import math
from collections import Counter


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def cosine_similarity(sent1, sent2):
    tokens1 = tokenize(sent1)
    tokens2 = tokenize(sent2)
    v1 = Counter(tokens1)
    v2 = Counter(tokens2)

    common = set(v1) & set(v2)
    dot = sum(v1[w] * v2[w] for w in common)

    mag1 = math.sqrt(sum(c * c for c in v1.values()))
    mag2 = math.sqrt(sum(c * c for c in v2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


def jaccard_similarity(sent1, sent2):
    s1 = set(tokenize(sent1))
    s2 = set(tokenize(sent2))
    if not s1 and not s2:
        return 1.0
    return len(s1 & s2) / len(s1 | s2)


def main():
    print("=" * 50)
    print("  SIMILARITY SCORE — Cosine + Jaccard")
    print("=" * 50)

    default1 = "The cat sat on the mat"
    default2 = "A cat is sitting on the mat"

    print(f"\nDefault sentence 1: '{default1}'")
    print(f"Default sentence 2: '{default2}'\n")

    s1 = input("Sentence 1 (Enter for default): ").strip() or default1
    s2 = input("Sentence 2 (Enter for default): ").strip() or default2

    cos = cosine_similarity(s1, s2)
    jac = jaccard_similarity(s1, s2)

    print(f"\nSentence 1: {s1}")
    print(f"Sentence 2: {s2}\n")
    print(f"Cosine Similarity  : {cos:.4f}   ({cos * 100:.2f}%)")
    print(f"Jaccard Similarity : {jac:.4f}   ({jac * 100:.2f}%)")

    print("\nInterpretation:")
    if cos > 0.8:
        print("  Sentences are VERY SIMILAR")
    elif cos > 0.5:
        print("  Sentences are MODERATELY SIMILAR")
    elif cos > 0.2:
        print("  Sentences have LOW similarity")
    else:
        print("  Sentences are DISSIMILAR")


if __name__ == "__main__":
    main()

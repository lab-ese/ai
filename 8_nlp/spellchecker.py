"""
Spell Checker — Edit Distance (Levenshtein) based suggestions

Run (Windows):
    python spellchecker.py
"""

import re


# Built-in dictionary of common English words
DICTIONARY = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there",
    "their", "what", "so", "up", "out", "if", "about", "who", "get",
    "which", "go", "me", "when", "make", "can", "like", "time", "no",
    "just", "him", "know", "take", "people", "into", "year", "your",
    "good", "some", "could", "them", "see", "other", "than", "then",
    "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first",
    "well", "way", "even", "new", "want", "any", "these", "give",
    "day", "most", "us", "world", "life", "hand", "part", "child",
    "eye", "woman", "place", "case", "week", "company", "system",
    "program", "question", "fact", "money", "lot", "right", "study",
    "book", "job", "word", "issue", "side", "kind", "head", "house",
    "service", "friend", "father", "power", "hour", "game", "line",
    "end", "member", "law", "car", "city", "community", "name",
    "president", "team", "minute", "idea", "kid", "body", "information",
    "parent", "face", "level", "office", "door", "health", "person",
    "art", "war", "history", "party", "result", "change", "morning",
    "reason", "research", "girl", "guy", "moment", "air", "teacher",
    "force", "education", "foot", "boy", "age", "policy", "process",
    "music", "market", "sense", "nation", "plan", "college", "interest",
    "death", "experience", "effect", "hello", "world", "computer",
    "python", "programming", "language", "code", "algorithm", "data",
    "science", "machine", "learning", "artificial", "intelligence",
    "spell", "check", "correct", "wrong", "right", "example", "test",
    "search", "find", "result", "answer", "problem", "solution",
}


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)

    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            ins = curr[j - 1] + 1
            dele = prev[j] + 1
            sub = prev[j - 1] + (ca != cb)
            curr.append(min(ins, dele, sub))
        prev = curr
    return prev[-1]


def suggest(word, max_suggestions=5):
    word = word.lower()
    if word in DICTIONARY:
        return None  # correctly spelled

    scored = [(levenshtein(word, w), w) for w in DICTIONARY]
    scored.sort(key=lambda x: (x[0], x[1]))
    return [w for _, w in scored[:max_suggestions]]


def main():
    print("=" * 50)
    print("  SPELL CHECKER — Edit Distance")
    print("=" * 50)
    print(f"Dictionary size: {len(DICTIONARY)} words\n")

    default = "Helo wrld this is a smple spel chek prgram"
    text = input("Sentence to check (Enter for default): ").strip() or default
    print(f"\nInput: {text}\n")

    words = re.findall(r"\b[a-zA-Z']+\b", text)

    print(f"{'Word':<18}{'Status':<14}{'Suggestions'}")
    print("-" * 60)

    misspelled = 0
    for word in words:
        sugg = suggest(word)
        if sugg is None:
            print(f"{word:<18}{'OK':<14}-")
        else:
            misspelled += 1
            print(f"{word:<18}{'MISSPELLED':<14}{', '.join(sugg)}")

    print(f"\nTotal words: {len(words)}  |  Misspelled: {misspelled}")


if __name__ == "__main__":
    main()

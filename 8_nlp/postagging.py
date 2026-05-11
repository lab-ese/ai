"""
POS Tagging — Natural Language Processing with NLTK

Install:
    pip install nltk

Run (Windows):
    python postagging.py
"""

import nltk

# Download required NLTK data (run once)
for pkg in ["punkt", "punkt_tab", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass


# Tag descriptions for cleaner output
TAG_NAMES = {
    "CC": "Conjunction", "CD": "Cardinal", "DT": "Determiner",
    "EX": "Existential", "FW": "Foreign", "IN": "Preposition",
    "JJ": "Adjective", "JJR": "Adj-Comp", "JJS": "Adj-Superl",
    "LS": "List", "MD": "Modal", "NN": "Noun-sing", "NNS": "Noun-pl",
    "NNP": "Proper-Noun", "NNPS": "Proper-Noun-pl", "PDT": "Predeterminer",
    "POS": "Possessive", "PRP": "Pronoun", "PRP$": "Pronoun-Poss",
    "RB": "Adverb", "RBR": "Adv-Comp", "RBS": "Adv-Superl",
    "RP": "Particle", "SYM": "Symbol", "TO": "to",
    "UH": "Interjection", "VB": "Verb", "VBD": "Verb-past",
    "VBG": "Verb-gerund", "VBN": "Verb-part", "VBP": "Verb-pres",
    "VBZ": "Verb-3sg", "WDT": "Wh-Det", "WP": "Wh-Pron",
    "WP$": "Wh-Pron-Poss", "WRB": "Wh-Adv",
}


def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    return nltk.pos_tag(tokens)


def main():
    print("=" * 50)
    print("  POS TAGGING — NLTK")
    print("=" * 50)
    print("Enter a sentence to tag (or press Enter for default)\n")

    default = "The quick brown fox jumps over the lazy dog."
    text = input("Sentence: ").strip() or default
    print(f"\nInput: {text}\n")

    tagged = pos_tag_sentence(text)

    print(f"{'Token':<15}{'Tag':<8}{'Description':<20}")
    print("-" * 43)
    for word, tag in tagged:
        desc = TAG_NAMES.get(tag, "")
        print(f"{word:<15}{tag:<8}{desc:<20}")

    print(f"\nTotal tokens: {len(tagged)}")


if __name__ == "__main__":
    main()

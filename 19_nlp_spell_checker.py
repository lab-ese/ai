import nltk

def simple_spell_checker(word, vocabulary):
    if word in vocabulary: return word, []
    candidates = [w for w in vocabulary if abs(len(w) - len(word)) <= 1 and w[0] == word[0]]
    suggestions = sorted(candidates, key=lambda w: nltk.edit_distance(word, w))[:3]
    return None, suggestions

if __name__ == "__main__":
    vocab = [
        "artificial", "intelligence", "algorithm", "python", "machine", 
        "learning", "photosynthesis", "technology", "heuristic", "constraint", 
        "search", "programming", "software", "database", "system"
    ]
    print("--- NLP: SPELL CHECKER ---")
    test = input("Enter Word: ").lower()
    correct, sug = simple_spell_checker(test, vocab)
    if correct: print(f"'{test}' is correct.")
    else: 
        if not sug: print(f"'{test}' is misspelled and no suggestions found.")
        else: print(f"Misspelled. Suggestions: {', '.join(sug)}")

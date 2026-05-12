import nltk

TAG_MAP = {
    'CC': 'Coordinating conjunction', 'DT': 'Determiner', 'IN': 'Preposition',
    'JJ': 'Adjective', 'NN': 'Noun, singular', 'NNP': 'Proper noun, singular',
    'NNS': 'Noun, plural', 'PRP': 'Personal pronoun', 'RB': 'Adverb',
    'VB': 'Verb, base form', 'VBD': 'Verb, past tense', 'VBG': 'Verb, gerund',
    'VBZ': 'Verb, 3rd person sing. present',
}

def perform_pos_tagging(sentence):
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('taggers/averaged_perceptron_tagger')
    except:
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('averaged_perceptron_tagger_eng', quiet=True)
    tokens = nltk.word_tokenize(sentence)
    return nltk.pos_tag(tokens)

if __name__ == "__main__":
    text = input("Enter a sentence: ") or "The quick brown fox jumps over the lazy dog."
    results = perform_pos_tagging(text)
    print(f"\n{'WORD':<15} | {'TAG':<6} | {'DESCRIPTION'}")
    print("-" * 45)
    for word, tag in results:
        print(f"{word:<15} | {tag:<6} | {TAG_MAP.get(tag, 'Other')}")

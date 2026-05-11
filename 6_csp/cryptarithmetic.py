"""
Cryptarithmetic — CSP with Backtracking (SEND + MORE = MONEY)

Run (Windows):
    python cryptarithmetic.py
"""

from itertools import permutations


def solve(word1, word2, result):
    letters = sorted(set(word1 + word2 + result))
    if len(letters) > 10:
        return None
    leading = {word1[0], word2[0], result[0]}

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[ch] == 0 for ch in leading):
            continue
        v1 = int("".join(str(mapping[c]) for c in word1))
        v2 = int("".join(str(mapping[c]) for c in word2))
        vr = int("".join(str(mapping[c]) for c in result))
        if v1 + v2 == vr:
            return mapping, v1, v2, vr
    return None


def main():
    print("=" * 40)
    print("  CRYPTARITHMETIC — CSP")
    print("=" * 40)
    print("Default puzzle: SEND + MORE = MONEY\n")

    w1 = input("Word 1 (default SEND): ").strip().upper() or "SEND"
    w2 = input("Word 2 (default MORE): ").strip().upper() or "MORE"
    wr = input("Result (default MONEY): ").strip().upper() or "MONEY"

    if not (w1.isalpha() and w2.isalpha() and wr.isalpha()):
        print("Words must be letters only.")
        return

    print(f"\nSolving: {w1} + {w2} = {wr} ...\n")
    sol = solve(w1, w2, wr)
    if sol is None:
        print("No solution found.")
        return

    mapping, v1, v2, vr = sol
    print("Letter -> Digit mapping:")
    for letter in sorted(mapping):
        print(f"  {letter} = {mapping[letter]}")

    width = len(wr) + 2
    print()
    print(f"    {w1:>{width}}        {v1:>{width}}")
    print(f"  + {w2:>{width}}      + {v2:>{width}}")
    print(f"    {'-' * width}        {'-' * width}")
    print(f"    {wr:>{width}}        {vr:>{width}}")


if __name__ == "__main__":
    main()

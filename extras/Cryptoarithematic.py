from itertools import permutations
import matplotlib.pyplot as plt


def solve_cryptarithm(w1, w2, res):

    letters = list(set(w1 + w2 + res))
    if len(letters) > 10:
        print("Too many unique letters")
        return None

    first_letters = {w1[0], w2[0], res[0]}
    digits = range(10)

    # Precompute positions (avoids repeated joins)
    def word_to_number(word, mapping):
        return sum(mapping[c] * (10 ** i) for i, c in enumerate(reversed(word)))

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Constraint 1: No leading zero
        if any(mapping[ch] == 0 for ch in first_letters):
            continue

        # Convert using faster method
        n1 = word_to_number(w1, mapping)
        n2 = word_to_number(w2, mapping)
        n3 = word_to_number(res, mapping)

        # Constraint 2: Equation satisfied
        if n1 + n2 == n3:
            return mapping, n1, n2, n3

    return None


def visualize_solution(w1, w2, res, n1, n2, n3):
    fig, ax = plt.subplots()

    text = (
        f"  {w1}\n"
        f"+ {w2}\n"
        f"------\n"
        f" {res}\n\n"
        f"  {n1}\n"
        f"+ {n2}\n"
        f"------\n"
        f" {n3}"
    )

    ax.text(0.1, 0.5, text, fontsize=16, family='monospace')
    ax.axis('off')

    plt.title("Cryptarithmetic Solution")
    plt.show()


# -------- INPUT --------
w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
res = input("Enter result word: ").upper()

solution = solve_cryptarithm(w1, w2, res)

if solution:
    mapping, n1, n2, n3 = solution

    print("\nSolution Found:\n")
    for k in sorted(mapping):
        print(k, "=", mapping[k])

    print("\nVerification:")
    print(n1)
    print("+", n2)
    print("=", n3)

    visualize_solution(w1, w2, res, n1, n2, n3)

else:
    print("No solution exists")
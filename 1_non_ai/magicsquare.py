"""
Magic Square — Siamese Method (Non-AI, Odd Order Only)

Run (Windows):
    python magicsquare.py
"""


def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Siamese method only works for ODD n")

    square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2  # start at top-center

    for num in range(1, n * n + 1):
        square[i][j] = num
        ni, nj = (i - 1) % n, (j + 1) % n   # move up-right
        if square[ni][nj] != 0:             # if filled, move down
            ni = (i + 1) % n
            nj = j
        i, j = ni, nj
    return square


def print_square(square, n):
    width = len(str(n * n)) + 1
    for row in square:
        print(" ".join(f"{x:>{width}}" for x in row))


def verify(square, n):
    target = n * (n * n + 1) // 2
    for row in square:
        if sum(row) != target:
            return False, target
    for c in range(n):
        if sum(square[r][c] for r in range(n)) != target:
            return False, target
    if sum(square[i][i] for i in range(n)) != target:
        return False, target
    if sum(square[i][n - 1 - i] for i in range(n)) != target:
        return False, target
    return True, target


def main():
    n = int(input("Enter odd order N: "))
    if n % 2 == 0:
        print("Error: N must be odd for Siamese method.")
        return

    square = generate_magic_square(n)
    print(f"\nMagic Square of order {n}:\n")
    print_square(square, n)

    ok, target = verify(square, n)
    print(f"\nMagic Constant: {target}")
    print(f"Verification: {'PASSED' if ok else 'FAILED'}")


if __name__ == "__main__":
    main()

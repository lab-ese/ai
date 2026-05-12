def solve_cryptarithmetic(word1, word2, result):
    letters = sorted(list(set(word1 + word2 + result)))
    if len(letters) > 10: return None
    assigned = [False] * 10; mapping = {}
    def is_valid():
        def get_val(w):
            n = 0
            for c in w: n = n * 10 + mapping[c]
            return n
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0: return False
        return get_val(word1) + get_val(word2) == get_val(result)
    def backtrack(idx):
        if idx == len(letters): return is_valid()
        char = letters[idx]
        for digit in range(10):
            if not assigned[digit]:
                mapping[char] = digit; assigned[digit] = True
                if backtrack(idx + 1): return True
                assigned[digit] = False; del mapping[char]
        return False
    if backtrack(0): return mapping
    return None

if __name__ == "__main__":
    print("--- CSP: CRYPTARITHMETIC ---")
    w1 = input("Word 1: ").upper(); w2 = input("Word 2: ").upper(); res = input("Result: ").upper()
    sol = solve_cryptarithmetic(w1, w2, res)
    if sol:
        for c in sorted(sol.keys()): print(f"{c} = {sol[c]}")
    else: print("No solution.")

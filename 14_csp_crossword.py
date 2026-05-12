def print_crossword(grid):
    if not grid:
        print("No solution found.")
        return
    n = len(grid)
    print("+" + "---+" * n)
    for row in grid:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * n)

def solve_crossword(words, slots, grid_size):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def can_place(word, slot, current_grid):
        r, c, length, orient = slot
        if len(word) != length:
            return False
        for i in range(length):
            nr, nc = (r, c + i) if orient == 'H' else (r + i, c)
            if current_grid[nr][nc] != ' ' and current_grid[nr][nc] != word[i]:
                return False
        return True

    def place_word(word, slot, current_grid):
        r, c, length, orient = slot
        char_replaced = []
        for i in range(length):
            nr, nc = (r, c + i) if orient == 'H' else (r + i, c)
            char_replaced.append(current_grid[nr][nc])
            current_grid[nr][nc] = word[i]
        return char_replaced

    def backtrack(slot_idx):
        if slot_idx == len(slots):
            return True
            
        current_slot = slots[slot_idx]
        for i in range(len(words)):
            word = words[i]
            if word and can_place(word, current_slot, grid):
                old_chars = place_word(word, current_slot, grid)
                words[i] = None
                if backtrack(slot_idx + 1):
                    return True
                words[i] = word
                # Restore old chars
                r, c, length, orient = current_slot
                for j in range(length):
                    nr, nc = (r, c + j) if orient == 'H' else (r + j, c)
                    grid[nr][nc] = old_chars[j]
        return False

    if backtrack(0):
        return grid
    return None

if __name__ == "__main__":
    # Updated word list with "EVADE" to ensure a valid solution exists for the puzzle slots
    word_list = ["APPLE", "ALIVE", "EVADE", "EAGLE", "EXTRA", "ADIEU"]
    puzzle_slots = [
        (0, 0, 5, 'H'), # Row 0, Cols 0-4
        (0, 0, 5, 'V'), # Col 0, Rows 0-4
        (0, 4, 5, 'V'), # Col 4, Rows 0-4
        (4, 0, 5, 'H')  # Row 4, Cols 0-4
    ]
    print("--- CROSSWORD SOLVER (CSP) ---")
    solution = solve_crossword(word_list, puzzle_slots, 5)
    print_crossword(solution)

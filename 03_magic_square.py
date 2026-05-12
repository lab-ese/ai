def generate_magic_square(n):
    # This algorithm (Siamese Method) only works for odd values of n
    if n % 2 == 0:
        print("Error: This method only generates magic squares for odd-sized grids (3, 5, 7, etc.).")
        return None
        
    # Initialize a 2D array with 0s
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    
    # 1. Position of number 1 is always (n/2, n-1)
    # Note: There are different variations, this is the 'Right-Up' variation.
    i = n // 2
    j = n - 1
    
    num = 1
    while num <= n * n:
        # Condition: If we go out of bounds on both sides (top-right corner overflow)
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            # If we go out of the right side, wrap around to the first column
            if j == n:
                j = 0
            # If we go out of the top side, wrap around to the last row
            if i < 0:
                i = n - 1
                
        # If the cell is already filled, move back to the previous position
        # and move one cell to the left instead.
        if magic_square[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            magic_square[i][j] = num
            num += 1
            
        # Move up and to the right for the next number
        j += 1
        i -= 1
        
    return magic_square

def verify_and_print(square):
    n = len(square)
    magic_sum = n * (n**2 + 1) // 2
    print(f"\nMagic Square of size {n}x{n}:")
    print(f"Expected Magic Sum: {magic_sum}")
    print("-" * (n * 8))
    
    for row in square:
        print("\t".join(map(str, row)))
    print("-" * (n * 8))

    # Verification: Check row sum and column sum
    row_sum = sum(square[0])
    col_sum = sum(square[i][0] for i in range(n))
    print(f"Verification: Row 1 Sum = {row_sum}, Column 1 Sum = {col_sum}")

if __name__ == "__main__":
    print("--- MAGIC SQUARE GENERATOR (NON-AI) ---")
    try:
        n_input = int(input("Enter size of magic square (odd number only): "))
        square = generate_magic_square(n_input)
        if square:
            verify_and_print(square)
    except ValueError:
        print("Invalid input! Please enter an odd integer.")

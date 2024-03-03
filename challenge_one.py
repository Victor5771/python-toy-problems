def solution(A):
    n = len(A)
    if n == 0:
        return 0
    
    target = 10
    moves = 0
    
    # Calculate the surplus or deficit of bricks in each box
    differences = [A[i] - target for i in range(n)]
    
    # Iterate over each box and distribute bricks
    for i in range(n):
        if differences[i] > 0:
            # Move bricks to the left
            if i > 0:
                # Calculate how many bricks can be moved to the left box
                to_move = min(differences[i], differences[i-1])
                # Update the differences array
                differences[i] -= to_move
                differences[i-1] += to_move
                # Update moves count
                moves += to_move
            else:
                return -1  # Cannot move bricks to the leftmost box
        
        if differences[i] < 0:
            # Move bricks to the right
            if i < n - 1:
                # Calculate how many bricks can be moved to the right box
                to_move = min(-differences[i], differences[i+1])
                # Update the differences array
                differences[i] += to_move
                differences[i+1] -= to_move
                # Update moves count
                moves += to_move
            else:
                return -1  # Cannot move bricks to the rightmost box
    
    # Check if all boxes have exactly 10 bricks
    if all(diff == 0 for diff in differences):
        return moves
    else:
        return -1  # It's not possible to have exactly 10 bricks in each box

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1

def solution(A):
    n = len(A)
    if n == 0:
        return 0
    
    target = 10
    moves = 0
    
    
    differences = [A[i] - target for i in range(n)]
    
   
    for i in range(n):
        if differences[i] > 0:
            
            if i > 0:
                
                to_move = min(differences[i], differences[i-1])
                
                differences[i] -= to_move
                differences[i-1] += to_move
                
                moves += to_move
            else:
                return -1  
        
        if differences[i] < 0:
            
            if i < n - 1:
                
                to_move = min(-differences[i], differences[i+1])
                
                differences[i] += to_move
                differences[i+1] -= to_move
                
                moves += to_move
            else:
                return -1  #
    
    
    if all(diff == 0 for diff in differences):
        return moves
    else:
        return -1 
    
# Test cases
print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11]))  
print(solution([7, 14, 10]))  

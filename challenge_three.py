def solution(N):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    for i in range(N):
        result += letters[i % 26]
    
    return result[:N]  

# Test cases
print(solution(3))  
print(solution(5))  
print(solution(30))  

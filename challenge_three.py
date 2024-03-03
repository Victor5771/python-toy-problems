def solution(N):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    for i in range(N):
        result += letters[i % 26]
    
    return result[:N]  # Adjusted to return only N characters

# Test cases
print(solution(3))  # Output: "abc"
print(solution(5))  # Output: "abcde"
print(solution(30))  # Output: "abcdefghijklmnopqrstuvwxyz"

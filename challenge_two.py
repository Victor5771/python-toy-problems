def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    digit_sums = {}
    max_sum = -1
    
    
    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits not in digit_sums:
            digit_sums[sum_digits] = []
        digit_sums[sum_digits].append(num)
    
    
    for key in digit_sums.keys():
        if len(digit_sums[key]) >= 2:
            max_sum = max(max_sum, sum(sorted(digit_sums[key])[-2:]))
            
    return max_sum

# Example usage:
print(solution([51, 71, 17, 42]))  
print(solution([42, 33, 60]))  
print(solution([51, 32, 43]))  
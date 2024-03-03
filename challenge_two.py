def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    digit_sums = {}
    max_sum = -1
    
    # Create a dictionary of numbers with the same digit sums
    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits not in digit_sums:
            digit_sums[sum_digits] = []
        digit_sums[sum_digits].append(num)
    
    # Find the maximum sum of two numbers with equal digit sums
    for key in digit_sums.keys():
        if len(digit_sums[key]) >= 2:
            max_sum = max(max_sum, sum(sorted(digit_sums[key])[-2:]))
            
    return max_sum

# Example usage:
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))  # Output: 102
print(solution([51, 32, 43]))  # Output: -1

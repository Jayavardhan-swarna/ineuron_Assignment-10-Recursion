def isPowerOfThree(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

# Example usage:
n = 27
result = isPowerOfThree(n)
print(result)  # Output: True 

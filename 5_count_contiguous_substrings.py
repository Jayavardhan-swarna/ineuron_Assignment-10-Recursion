def count_contiguous_substrings(S):
    count = 0
    n = len(S)

    # Iterate through each character in the string
    for i in range(n):
        # Count substrings where S[i] is the starting and ending character
        count += 1

        # Expand the substring from S[i] to the left and right
        left = i - 1
        right = i + 1

        while left >= 0 and right < n and S[left] == S[right]:
            count += 1
            left -= 1
            right += 1

    return count


S = "abcab"
count = count_contiguous_substrings(S)
print(count) 

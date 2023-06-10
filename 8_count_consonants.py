def count_consonants(string):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

string = "abc de"
result = count_consonants(string)
print(result) 

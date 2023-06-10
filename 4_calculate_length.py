def calculate_length(string):
    if string == "":
        return 0
    return 1 + calculate_length(string[1:])


string = "abcd"
length = calculate_length(string)
print(length) 

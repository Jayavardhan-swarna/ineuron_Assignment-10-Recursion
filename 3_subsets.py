def subsets(set_str):
    subsets_helper(set_str, "", 0)

def subsets_helper(set_str, current_subset, index):
    if index == len(set_str):
        print(current_subset)
        return
    
    subsets_helper(set_str, current_subset, index + 1)
    subsets_helper(set_str, current_subset + set_str[index], index + 1)

set_str = "abc"
subsets(set_str) 

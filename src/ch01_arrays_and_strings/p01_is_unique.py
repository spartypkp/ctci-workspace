"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


# All unique characters



# Brute Force:
# Sort the string, then iterate through checking if any 2 neighboring characters are the same

# "hello mark" -> " ll" 

# slog(s) + o(s)
def is_unique(string: str):
    sorted_string = sorted(string)

    for i, ch in enumerate(sorted_string):
        # Reached last item
        if(i == len(sorted_string)-1):
            break
        # Next element is equal to current
        if ch == sorted_string[i+1]:
            print(f"String {string} is not unique!")
            return False
    print(f"String {string} is unique!")
    return True


def main():
    test_1 = "hello mark" # "hello mark" -> False
    test_2 = "abcdefghi" # abcdefghi" -> True
    test_3 = "" # true
    test_4 = "aaaaaaaa" # false

    result_1 = is_unique(test_1)
    if result_1:
        print(f"Error! Result_1 should be false!")
    
    result_2 = is_unique(test_2)
    if not result_2:
        print(f"Error! Result_2 should be true!")

    result_3 = is_unique(test_3)
    if not result_3:
        print(f"Error! Result_3 should be true!")
    
    result_4 = is_unique(test_4)
    if result_4:
        print(f"Error! Result 4 should be false")



if __name__ == "__main__":
    main()

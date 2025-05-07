"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
EXAMPLE
Input: "Mr John Smith "
, 13
Output: "Mr%20John%20Smith"
"""

# Python strings are immutable.
# Clarification: "__" -> "%20%20"
# Tabs, other chars need to be replaced?
# Implement as array of chars in Python?


# Pythonic
# use the .replace() string method (Built in!)
# Probably the fastest method

# Brute Force
# Create a new array with 
# Iterate over

# This is really stupid - not meant for Python

def main():
    
    string_1 = "Test"
    answer_1 = "Test"
    result_1 = urlify(string_1)
    if result_1 != answer_1:
        print(f"Test 1 failed!")
    
    string_2 = "Test string"
    answer_2 = f"Test%20string"
    result_2 = urlify(string_2)
    if result_2 != answer_2:
        print(f"Test 2 failed!")


def urlify(string: str):
    return string.replace(" ", "%20")

if __name__ == "__main__":
    main()
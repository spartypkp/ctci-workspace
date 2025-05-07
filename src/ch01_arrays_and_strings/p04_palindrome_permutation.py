"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""



# Ignore white space? Yes
# Case insesitive. Yes

# Not limited to dictionary words? All potential characters ASCII? ',.z/.xz' punctuation, etc...

# Assume that we can ignore white space - and should be case insesitive

## What makes a valid palindrome - same forwards and backwards
# Character Counts: All must be even (Allow for 1 non-even IF length of string is odd)

def main():
    # string: "aabbc" could be palindrome: "abcba"  -> True
    # 2 a, 2 b, 1 c Length (5)
    string_1 = "aAbBc"
    result_1 = True
    if is_palindrome_permutation(string_1) != result_1:
        print(f"Test 1 Failed!")
    

    # string: "ac" can NOT be any palindrome -> False
    string_2 = "ac"
    result_2 = False
    if is_palindrome_permutation(string_2) != result_2:
        print(f"Test 2 Failed!")

    string_3 = " aaccerr"
    result_3 = True
    if is_palindrome_permutation(string_3) != result_3:
        print(f"Test 3 Failed!")


    string_4 = "askldjfhkasdhg;lkfna jsdkhfaslkfh lkjah23678rq8679801tuoihqjagdskbgvsnkv.,ncm nz"
    result_4 = False
    if is_palindrome_permutation(string_4) != result_4:
        print(f"Test 4 Failed!")


    # ""
    # "           "
    # "a          "


# S is length of string
# O(s) + O(s)
def is_palindrome_permutation(string: str):
    print(f"Checking if '{string}' is palindrome permutation!")
    # Get the count of all characters in dictionary { 'char': count } (ignore space)
    # { 'a': 2, 'b': 2, 'c': 1}
    counts = {}
    for i, char in enumerate(string):
        ch = char.lower()
        if ch == " ":
            continue
        if ch not in counts:
            counts[ch] = 1
        else:
            del counts[ch]
    # If more than one key with odd value: False, else True
    #print(counts)
    #print(len(counts.keys()))
    print(len(counts.keys()) <= 1)
    return len(counts.keys()) <= 1
            


if __name__ == "__main__":
    main()
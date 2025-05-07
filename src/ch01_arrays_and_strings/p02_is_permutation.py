"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

# Meaning of Permutation: string A could be re-arranged to equal string B

# A and B must be the same size!
# A and B must contain the same chars at same occurence

# Brute Force Algorithm
# Create a dictionary { 'char' : count}
# Loop through string A - add all chars (and increment count)
# Loop through string A  - decrement count (remove key) if needed

# Is the dictionary empty? If so - that's a valid permutation


# a: "will" b: "mark" -> False
# a: "abc" b: "cba" -> True
# a: "abc" b: "dcba" -> False


def main():
    a_1 = "will"
    b_1 = "mark"
    answer_1 = False
    
    result_1 = is_permutation(a_1, b_1)
    if result_1 != answer_1:
        print(f"Test 1 Failed!")

    a_2 = "abc"
    b_2 = "cba"
    answer_2 = True

    result_2 = is_permutation(a_2, b_2)
    if result_2 != answer_2:
        print(f"Test 2 Failed")

    a_3 = "abc"
    b_3 = "dcba"
    answer_3 = False

    result_3 = is_permutation(a_3, b_3)
    if result_3 != answer_3:
        print(f"Test 3 failed")

    # Interesting case
    a_4 = ""
    b_4 = ""
    answer_4 = True

    result_4 = is_permutation(a_4, b_4)
    if result_4 != answer_4:
        print(f"Test 4 failed")

# n is size of a & b (immediately fails in O(1) if not true)
# Time complexity: O(n) 
# Space complexity: O(a)

def is_permutation(a: str, b: str):
    
    print(f"Is String A: {a} a permutation of String B: {b}?")
    if (len(a) != len(b)):
        print(f"Not a permutation! (input strings must have same length)")
        return False
    # Could use defaultdict here
    counts = {}
    # Add all unique chars with count of 1, increment already seen
    for i, ch in enumerate(a):
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1


    for i, ch in enumerate(b):
        # Character in B but NOT in A
        if ch not in counts:
            print(f"Not a permutation! (String B has char not in A)")
            return False
        
        # Remoe the key 
        if counts[ch] == 1:
            del counts[ch]
        # Decrement the value
        else:
            counts[ch] -= 1
    
    # If counts has any keys it will return True, False if empty.
    # An empty dict means valid permutation
    if counts:
        print(f"Is a permutation!")
        return True
    else:
        print(f"Not a permutation! (String A has char not in B)")
        return False
   



if __name__ == "__main__":
    main()
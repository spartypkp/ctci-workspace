"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

# insert, remove, replace
# One edit away (or equal)

# Ways to Fail This
# | len(A) - len(B) | > 1  Lengths are too different

# Char count difference > 1

# Two Pointers
# pale
# ple

# Check for immediate fails
# Iterate through strings
# if equal, move pointer for both
# If not equal - perform operation if you can or return false

def main():
    a_1 = "pale"
    b_1 = "ple"
    result_1 = True
    if check_one_away(a_1, b_1) != result_1:
        print(f"Test 1 failed!")

    a_2 = "pales"
    b_2 = "pale"
    result_2 = True
    if check_one_away(a_2, b_2) != result_2:
        print(f"Test 2 failed!")
    
    a_3 = "pale"
    b_3 = "bale"
    result_3 = True
    if check_one_away(a_3, b_3) != result_3:
        print(f"Test 3 failed!")

    a_4 = "pale"
    b_4 = "bake"
    result_4 = False
    if check_one_away(a_4, b_4) != result_4:
        print(f"Test 4 failed!")


    a_5 = ""
    b_5 = ""
    result_5 = True
    if check_one_away(a_5, b_5) != result_5:
        print(f"Test 5 failed!")

    a_6 = ""
    b_6 = "asd;kfhkdlajshdflkjsahflkjdshakljsdfhlkjasd"
    result_6 = False
    if check_one_away(a_6, b_6) != result_6:
        print(f"Test 6 failed!")

# o(A) time
# o(1) space
def check_one_away(a: str, b:str):
    print(f"Checking if a: '{a}' is one away from '{b}'.")
    # immediate success
    if a == b:
        print(f"One move away - are equal!")
        return True
    # immediate fails
    if abs(len(a) - len(b)) > 1:
        print(f"Not one move away - string legnth diff")
        return False
    
    a_len = len(a)
    b_len = len(b)
    
    operations = 0
    
    a_ptr = 0
    
    b_ptr = 0

    while a_ptr < a_len or b_ptr < b_len:
        # Edge case (a reached end)
        if a_ptr == a_len or b_ptr == b_len:
            # Can you remove the last one?
            print(f"Is one away: {operations == 0}")
            return operations == 0
        # Equal, continue
        if a[a_ptr] == b[b_ptr]:
            a_ptr += 1
            b_ptr += 1
            continue

        # Not Equal Cases
        if operations == 1:
            print(f"Is one away: False")
            return False
        operations += 1
        # Equal length strings (one must be replaced)
        if a_len == b_len:
            a_ptr += 1
            b_ptr += 1
            continue

        # Not equal strings, delete from longer
        if a_len > b_len:
            a_ptr += 1
        else:
            b_ptr +=1
    # Default
    print(f"Is one away: True")
    return True
        





if __name__ == "__main__":
    main()



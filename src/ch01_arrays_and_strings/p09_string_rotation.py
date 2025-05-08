"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat").
"""

# isSubstring(s1, s2)
# Only one call 

# rotation 

# "wat_erbottlewat_erbottle"

def main():
    input_1 = ("waterbottle", "erbottlewat")
    answer_1 = True
    result_1 = is_rotation(*input_1)

    if (answer_1 != result_1):
        print(f"Test 1 failed!")

    input_2 = ("waterbottle", "asdf")
    answer_2 = False
    result_2 = is_rotation(*input_2)

    if (answer_2 != result_2):
        print(f"Test 2 failed!")


    input_3 = ("aaaaab", "bbaaaa")
    answer_3 = False
    result_3 = is_rotation(*input_3)

    if (answer_3 != result_3):
        print(f"Test 3 failed!")

    input_4 = ("", "")
    answer_4 = True
    result_4 = is_rotation(*input_4)

    if (answer_4 != result_4):
        print(f"Test 4 failed!")

def is_rotation(s1: str, s2: str):
    print(f"Checking if s1: {s1} is a rotation of s2: {s2}!")
    if len(s1) != len(s2):
        print(f"False")
        return False
    check_string = f"{s1}{s1}"
    # 0 or 1 (this is isSubstring)
    result = check_string.count(s2)
    print(result == 1)
    return result

if __name__ == "__main__":
    main()
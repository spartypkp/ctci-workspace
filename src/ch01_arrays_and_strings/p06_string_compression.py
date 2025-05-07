"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

# Q: 
# 'aaAA' -> 'a4' or 'a2A2' Second

# Worst case
# 'abcd' -> 'a1b1c1d1' length of 4 -> 8


# 'a1b1c1d1'

# Brute Force
# Commpress the string by making new string then check if its longer than original
# ''
# iterate through - keep track of current char and count.
# - if same, increment count
# - if not, add to new string and reset
# Make sure to add from end

# What would make the strings exactly equal in length?


def main():
    string_1 = 'aabb'
    compressed_1 = '2a2b'
    # Average repeated char == 2

    # avg = 4
    string_2 = 'aaaabbbb'
    compressed_2 = '4a4b'

    # avg < 2
    string_3 = 'hajdsfkaaaaaaa'
    compressed_3 = 'h1a1j1d1s1f1k1a7'

    string_4 = 'abcdefg'


def compression(string: str):
    # Could never compress 2 string better
    if len(str) < 2:
        return string
    
    compressed_string = ''
    repeated_chars = 4

    current_count = 1
    current_char = string[0]
    for i, ch in enumerate(string):
        # Just to start at 1 (and keep enumerate)
        if i == 0:
            continue
        # Consecutive char - continue
        if ch == current_char:
            current_count += 1
            continue
        else:
            compressed_string += f"{current_char}{current_count}"
            current_count = 1
            current_char = ch
    # Handle last element
    compressed_string += f"{current_char}{current_count}"

    if len(compressed_string) >= len(string):
        return string
    else:
        return compressed_string



if __name__ == "__main__":
    main()




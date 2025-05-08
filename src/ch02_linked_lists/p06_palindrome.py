from typing import List
"""
Palindrome: Implement a function to check if a linked list is a palindrome.
Hints:#5, #13, #29, #61, #101
"""

# string (char)
# singly or doubly linked?
# Head only?

class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None

def create_linked_list(values: List[str]):
    if len(values) == 0:
        return 0

    node = Node(values[0])
    iterator = node

    for i in range(1, len(values)):
        new_node = Node(values[i])
        iterator.next = new_node
        iterator = iterator.next
    return node

def print_linked_list(node: Node):
    result = ""
    iterator = node
    while iterator:
        result += f"[{iterator.val}]"
        if iterator.next:
            result += "->"
        iterator = iterator.next
    print(result)
    return result


def main():
    input_1 = create_linked_list(["a", "b", "b", "a"]) # True
    print_linked_list(input_1)
    result_1 = is_palindrome(input_1)
    print(result_1)

    input_2 = create_linked_list(["d", "z", "x", "y"]) # False
    print_linked_list(input_2)
    result_2 = is_palindrome(input_2)
    print(result_2)


    input_3 = create_linked_list(["z", "z", "z"]) # True
    print_linked_list(input_3)
    result_3 = is_palindrome(input_3)
    print(result_3)

    input_4 = create_linked_list(["z"]) # True
    print_linked_list(input_4)
    result_4 = is_palindrome(input_4)
    print(result_4)


    



# Recursive helper needed!
# o(n) time o(n) space
def is_palindrome(node: Node):
    start_iterator = node
    end_iterator = node


    def is_palindrome_helper(sub_node: Node):
        nonlocal start_iterator
        # Find the end!
        if sub_node is None:
            return None
        # Previous check was valid? Or still ongoing
        valid_palindrome = is_palindrome_helper(sub_node.next)
        #print(f"Start: {start_iterator.val}, end: {sub_node.val}. Still valid: {valid_palindrome}")
        if valid_palindrome is None:

            # Exit Case: Iterators Equal Each other (odd case)
            if start_iterator == sub_node:
                #print(F"Exit Case: Iterators Equal Each other (odd case)")
                return True

            # Check start and end_iterator vals for equality
            if start_iterator.val != sub_node.val:
                #print(F"start and end_iterator are not equal")
                return False
            
            # Exit Case: Iterators next to each other!
            if start_iterator.next == sub_node:
                #print(f"Exit Case: Iterators next to each other!")
                return True
            
            start_iterator = start_iterator.next
            return None
        else:
            return valid_palindrome

    return is_palindrome_helper(end_iterator)
    


if __name__ == "__main__":
    main()
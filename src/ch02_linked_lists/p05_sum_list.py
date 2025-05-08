from typing import List
"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
"""

# Singly or doubly?

# Head and tail or just head of both?

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def create_linked_list(values: List[int]):
    if len(values) == 0:
        return None
    
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

    input_1 = create_linked_list([3, 2, 1]) # 123
    input_2 = create_linked_list([9, 9, 9]) # 999
    # Answer [2, 2, 1, 1] (1122)
    result = sum_lists(input_1, input_2)
    print_linked_list(result)

def sum_lists(list_1: Node, list_2: Node):
    # Choose list_1 as the list to modify
    current = list_1
    head = list_1  # Save the head to return later
    
    l1 = list_1
    l2 = list_2
    carry = 0
    
    # Keep track of the tail of result list
    prev = None
    
    # Loop while we have nodes to process
    while l1 or l2 or carry:
        # Get values (0 if node doesn't exist)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        
        if l1:
            # If l1 exists, modify it in place
            l1.val = digit
            prev = l1
            l1 = l1.next
        else:
            # If l1 is done but we still have l2 or carry,
            # create a new node and append to prev
            new_node = Node(digit)
            prev.next = new_node
            prev = new_node
        
        # Move l2 if it exists
        if l2:
            l2 = l2.next
    
    return head 

        
        

    

if __name__ == "__main__":
    main()

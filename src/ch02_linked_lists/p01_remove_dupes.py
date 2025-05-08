from typing import List
"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_linked_list(node: Node):
    result = ""
    iterator = node
    while iterator:
        result += f"[{iterator.val}]"
        if iterator.next:
            result += "->"
        iterator = iterator.next
        
    return result
    
# Helper
def create_linked_list(array: List[int]):
    if len(array) == 0:
        return None
    
    node = Node(val=array[0])

    pointer = node
    for i in range(1, len(array)):
        new_node = Node(val=array[i])
        pointer.next = new_node
        pointer = pointer.next
    
    return node


# single or doubly linked?

# Unsorted makes it more difficult 
# What kind of values are the nodes? (int)

def main():
    # [1] [2] [3] [4] -> [1] [2] [3] [4]
    input_1 = create_linked_list([1, 2, 3, 4])
    answer_1 = create_linked_list([1, 2, 3, 4])
    result_1 = remove_dupes_no_buffer(input_1)
    print(f"Answer: {print_linked_list(answer_1)}")
    
    
    # [1] [5] [1] [2] -> [5] [1] [2] OR [1] [5] [2]
    input_2 = create_linked_list([1, 5, 1, 2])
    answer_2 = create_linked_list([1, 5, 2])
    result_2 = remove_dupes_no_buffer(input_2)
    print(f"Answer: {print_linked_list(answer_2)}")

    # [10] [10] -> [10]
    input_3 = create_linked_list([10, 10])
    answer_3 = create_linked_list([10])
    result_3 = remove_dupes_no_buffer(input_3)
    print(f"Answer: {print_linked_list(answer_3)}")

    # [1] [1] [1] [1] [1] [1] [1] [1]
    input_4 = create_linked_list([1, 1, 1, 1, 1, 1, 1, 1, 1])
    answer_4 = create_linked_list([1])
    result_4 = remove_dupes_no_buffer(input_4)
    print(f"Answer: {print_linked_list(answer_4)}")

# O(n) time (n is number of nodes in original linked list)
# O(n) space. Worst case is all nodes are unique - dictionary with N keys
def remove_dupes(node: Node):
    print(f"Removing duplicates from {print_linked_list(node)}")
    # dictionary
    seen = {node.val: True}
    
    iterator = node
    # iterate through - check for membership in dictionary, remove if already in it.
    while iterator.next:
        #print(f"Iterator.val: {iterator.val}")
        if iterator.next.val in seen:
            # Skip
            skip = iterator.next.next
            iterator.next = skip
            # Cannot continue 
        else:
            iterator = iterator.next
    print(f"De-duplicated linked list: {print_linked_list(node)}")
    return node


def check_unique(node: Node, pointer: Node):
    iterator = node
    while iterator != pointer:
        if iterator.val == pointer.val:
            return False
        iterator = iterator.next
    return True

def remove_dupes_no_buffer(node: Node):
    print(f"Removing duplicates from {print_linked_list(node)}")
    
    iterator = node
    while iterator.next:
        # Check if it's unique
        is_unique = check_unique(node, iterator)
        if not is_unique:
            # Skip
            skip = iterator.next.next
            iterator.next = skip
            # Cannot continue 
        else:
            iterator = iterator.next
    print(f"De-duplicated linked list: {print_linked_list(node)}")
    return node

    

if __name__ == "__main__":
    main()
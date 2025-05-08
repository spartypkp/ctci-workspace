from typing import List
"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5] 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""


class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

def create_linked_list(array: List[int]):
    if len(array) == 0:
        return None
    
    node = Node(array[0])
    iterator = node
    for i in range(1, len(array)):
        new_node = Node(array[i])
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
    # Single or double? Single. Int values okay? 
    # What happens when X in list vs not?

    # 1 -> 5 -> 2 -> 4 [partition = 3]
    input_1 = create_linked_list([1, 5, 2, 4])
    partition_1 = 3
    new_list = partition(input_1, partition_1)
    print(f"Result:")
    print_linked_list(new_list)

    input_2 = create_linked_list([1, 1, 1, 1, 1])
    partition_2 = 10
    new_list = partition(input_2, partition_2)
    print(f"Result:")
    print_linked_list(new_list)

def partition(node: Node, partition: int):
    print(f"Partioning List:")
    print_linked_list(node)
    left = None
    left_iterator = None
    right = None
    right_iterator = None
    
    iterator = node
    while iterator:
        #print(f"iterator.val: {iterator.val}")
        if iterator.val < partition:
            #print(F"Left is defined: {left is not None}")
            if not left:
                left = iterator
                left_iterator = iterator
            else:
                left_iterator.next = iterator
                left_iterator = left_iterator.next
        else:
            if not right:
                right = iterator
                right_iterator = iterator
            else:
                right_iterator.next = iterator
                right_iterator = right_iterator.next
        iterator = iterator.next

    left_iterator.next = right
    return left


if __name__ == "__main__":
    main()
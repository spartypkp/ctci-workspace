from typing import List
"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129
"""

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
    iterator = node
    result = ""
    while iterator:
        result += f"[{iterator.val}]"
        if iterator.next:
            result += "->"
        iterator = iterator.next
    print(result)
    return result

def main():
    l1 = create_linked_list([1, 2, 3, 4])
    r1 = create_linked_list([3, 4])
    print("L1")
    print_linked_list(l1)
    print("R1")
    print_linked_list(r1)
    print(is_intersection(l1, r1)) # SHOULD BE FALSE

    reference = l1.next.next.next
    print(is_intersection(l1, reference)) # SHOULD BE TRUE


    # [1, 2, 3, 4]   [9, 2]

    # By reference NOT value
    # Python is operator

def is_intersection(l: Node, r: Node):
    # Get length of both
    length_l = 0
    iterator_l = l
    while iterator_l:
        length_l += 1
        iterator_l = iterator_l.next

    length_r = 0
    iterator_r = r
    while iterator_r:
        length_r += 1
        iterator_r = iterator_r.next

    advance_l = length_l - min(length_l, length_r)
    advance_r = length_r - min(length_l, length_r)

    # Start both pointers the same distance from the end (min length of lists)
    iterator_l = l
    for i in range(0, advance_l):
        iterator_l = iterator_l.next
    iterator_r = r
    for i in range(0, advance_r):
        iterator_r = iterator_r.next
   
    # if 'node' is 'node'
    while iterator_r:
        if iterator_r is iterator_l:
            return True
        iterator_r = iterator_r.next
        iterator_l = iterator_l.next
    return False

if __name__ == "__main__":
    main()
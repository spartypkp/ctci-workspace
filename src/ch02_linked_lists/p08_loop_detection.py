from typing import List
"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
Hints: #50, #69, #83, #90
"""

# Circular: Will infinitely traverse
# Non-circular: eventually next node will be None

# singly linked?
# Int value
class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None

def create_linked_list(values: List[str]):
    if len(values) == 0:
        return None
    
    head = Node(values[0])
    iterator = head
    for i in range(1, len(values)):
        new_node = Node(values[i])
        iterator.next = new_node
        iterator = iterator.next
    return head



def main():
    # [A] [B] -> [A]
    l1 = create_linked_list(["A", "B"])
    print(f"Pre-circular: ", ["A", "B"])
    # Make circular
    l1.next.next = l1
    print(f"Is circular: {is_circular(l1)}")

    # [A] [B] [C]
    l2 = create_linked_list(["A", "B", "C"])
    print(f"Valid list [\"A\", \"B\", \"C\"]")
    print(f"Is circular: {is_circular(l2)}")

    l3 = create_linked_list(["Z"])
    l3.next = l3
    print(f"Pre-circular: ", ["Z"])
    print(f"Is circular: {is_circular(l3)}")
    
    # Slow and Fast pointer
    # [A] [B] [C] [D] [E] -> [B]
def is_circular(node: Node):
    # 1 length lists - no next
    if node.next is None:
        #print(f"1 legnth no next case")
        return False
    # 1 length circular reference
    if node.next is node:
        #print(f"1 lenght circular case!")
        return True
    
    slow = node
    fast = slow.next
    # Valid linked list detection
    while fast and fast.next:
        # Circular detection
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


if __name__ == "__main__":
    main()
from typing import List
"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

# Node(val: int)
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

def main():
    # singly linked important
    # kth to last [1] [2] [3] [4]
    # - k = 0: LAST [4]
    # - k = 1: LAST-1 position [3]
    # - k = 1000: ? 
    input_1 = create_linked_list([1, 2, 3, 4]) 
    k_1 = 1
    print(f"Kth to last: {print_linked_list(input_1)} with k={k_1}")
    answer_1 = Node(4)
    result_1 = kth_to_last(input_1, k_1)
    print(f"Correct Answer: {print_linked_list(answer_1)}")
    print(f"Actual: {print_linked_list(result_1)}")
    

    input_2 = create_linked_list([1, 2, 3, 4])
    k_2 = 2
    print(f"Kth to last: {print_linked_list(input_2)} with k={k_2}")
    answer_2 = create_linked_list([3, 4])
    result_2 = kth_to_last(input_2, k_2)
    print(f"Correct Answer: {print_linked_list(answer_2)}")
    print(f"Actual: {print_linked_list(result_2)}")


# O(n) time
# O(1) space 
def kth_to_last(node: Node, k: int):
    slow = node
    fast = node
    count = k
    while fast.next and count > 0:
        fast = fast.next
        count -= 1
    #print(print_linked_list(slow))
    #print(print_linked_list(fast))
    # Advance both
    while fast:
        if fast.next is None:
            return slow.next
        slow = slow.next
        fast = fast.next
    return slow
    
if __name__ == "__main__":
    main()


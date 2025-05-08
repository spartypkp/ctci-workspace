from typing import List
"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f
"""
# Node
class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None


def create_linked_list(values: List[str]):
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
        #print(type(iterator))
        #print(f"{iterator.val}")
        result += f"[{iterator.val}]"
        if iterator.next:
            result += "->"
        iterator = iterator.next
    return result

def main():
    full_list = create_linked_list(["a", "b", "c", "d","e","f"])
    print(full_list)

    print(f"Before: {print_linked_list(full_list)}")
    node_to_delete = full_list.next.next
    delete_middle(node_to_delete)
    print(f"After: {print_linked_list(full_list)}")

    # c->d->e->f
    # a->b->d->e->f


def delete_middle(node: Node):
    # Don't allow deletion from end (1 node middle)
    if node is None:
        return None
    
    to_return = node.val
    node.val = delete_middle(node.next)
    # Make sure to clean up last element
    if node.next.val is None:
        node.next = None
    return to_return

    

if __name__ == "__main__":
    main()
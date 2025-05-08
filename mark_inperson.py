
from typing import List, Union
# 

def main():
    # list_1 = [["c", ["d", [[]], "x"]], "a", "b"]
    # answer_1 = ["c", "d", "x", "a", "b"]
    # print(f"Flattening list: {list_1}")
    # result = flatten(list_1, [])
    # print(f"Result:\n{result}")
    # if result != answer_1:
    #     print(f"Failed test 1!")

    list_1 = ["a", ["b"], [[["c"], ["z"]],[[[[["99"]]]], [] ]], "c"]
    answer_1 = ["a", "b", "c", "z", "99", "c"]
    print(f"Flattening list: {list_1}")
    result = iterative_flatten(list_1)
    print(f"Result:\n{result}")
    if result != answer_1:
        print(f"Failed test 1!")

    
# No recursion
# ["a", [["b"], "c"]] O(N) O(N^2) Space: O(N)
def iterative_flatten(array: Union[str, List[Union[str, List]]]):
    index = 0
    while index < len(array) - 2:
        next_element = array[index+1]
        print(f"Index: {index}, array: {array}")
        print(f"Next element: {next_element}")
        if isinstance(next_element, list):
            beginning = array[0:index+1]
            # Might have to check for accidental out of bounds
            end = []
            if index+2 != len(array):
                end = array[index+2:]
            print(f"End: {end}")

            beginning.extend(next_element)
            beginning.extend(end)
            array = beginning
            # Make sure we handle end of array ["a", ["b"]]
        else:
            index += 1
    return array
            
    # ["a", "a1", ["b"], "c"]
    # index 1
    # Look ahead 
    # type list
        # Get the beginning elements already checked [0:2]
        # Get the ending elements AFTER the look ahead if it exists
        # new_list = start.extend(next_element).extend(end) [3:]
    # 


def flatten(element: Union[str, List[Union[str, List]]], result: List):
    
    # Element is string, return
    if isinstance(element, str):
        result.append(element)
        return result
    # Empty list -> return without doing anything
    # if len(element) == 0:
    #     return result
    
    # Must be list
    for i, sub_element in enumerate(element):
        flatten(sub_element, result)
    return result
    

    



if __name__ == "__main__":
    main()
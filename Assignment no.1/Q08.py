# Function to reverse a list using a for loop and slicing; compare with tuples (immutable).

def reverse_list_for_loop(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):  # start from last index to 0
        reversed_list.append(lst[i])
    return reversed_list

numbers = [1, 2, 3, 4, 5]
print(reverse_list_for_loop(numbers))
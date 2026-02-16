# Write a function that takes a list and returns a new list with only unique elements using a set.

def get_element(input):
    return list(set(input)) # using set() to remove duplicates and directly convert back to list

list1 = ["apple", "banana", "apple", "orange", "banana", "grape"]

print("----- Orignal list------")
print(list1)

unique_list1 = get_element(list1) # Call the function and store the result
print("------UNIQUE LIST------")
print(f"unique elements: {unique_list1}")
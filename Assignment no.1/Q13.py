# Use list comprehension with if to filter even numbers from 1-50 into a tuple.

# Using list comprehension with condition
even_numbers = tuple([num for num in range(1, 51) if num % 2 == 0])

print(even_numbers)
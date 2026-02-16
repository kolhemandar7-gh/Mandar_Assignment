# Create a list of 10 numbers, loop to find and print the maximum using only conditionals (no max()).

number= [10, 23, 46, 98, 55, 61, 71, 100, 98, 1]   # list of 10 number

max = number[0] # first no. in list

for i in range(len(number)):  
    if number[i] > max:    # compare current element with max
        max = number[i]

print(f"Maximum number is {max}")
# Use nested for loops and if to print a multiplication table (1-10) as a list of tuples.

multiplication_table= []                   # empty list

for i in range(1, 11):                     #outer loop (1-10)
    for j in range(1, 11):                #inner loop (1-10)

        if i>=1 and j>=1:
            multiplication_table.append((i,j, i*j))

print(multiplication_table)

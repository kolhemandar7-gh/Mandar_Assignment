# Given list of scores, use while loop and conditionals to count passing (>=60) vs failing.

def count_R(Marks):
    passing = 0
    failing = 0
    i = 0

    while i < len(Marks):
        if Marks[i]>= 60:
            passing += 1
        else:
            failing += 1
        i += 1                       # Move to the next index
    return passing, failing          # Return total passing and failing counts
    
Marks= [75, 45, 90, 58, 62, 30, 80, 78, 34]
pass_count, fail_count = count_R(Marks)     # Call the function and store results

print("Passing:", pass_count)
print("Failing:", fail_count)
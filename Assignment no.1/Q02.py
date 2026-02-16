#Use if-elif-else to classify a number as positive, negative, or zero; test in a for loop over a list.

def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
    
num = [11, 26, -65, 0, -46, 97, 0]  

# creating the loop

for num in num:
    result = classify_number(num)
    print(f"{num} is {result}")

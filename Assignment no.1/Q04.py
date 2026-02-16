# Define a tuple of fruits; use a for loop to print those starting with 'A' or 'B'.

fruits=("Apple", "Banana", "Mango", "Avocado", "Berry", "Orange", "Grapes")

for F in fruits:
    if F.startswith("A") or F.startswith("B"):   # Check if the fruit starts with 'A' or 'B'
         print(F)
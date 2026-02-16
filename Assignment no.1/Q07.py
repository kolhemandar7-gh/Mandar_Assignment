#Create a dictionary of {name: age}; loop to print adults (>=18) using items().

friends= {"Mandar":23, "Tejas":22, "Raj":16, "Yash":30, "Nitesh":17, "Kunal":18}

print("Adults list")

for name, age in friends.items():
    if age >=18:
        print(f"{name} -> {age}")
 
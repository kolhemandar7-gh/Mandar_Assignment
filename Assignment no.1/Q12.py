# Dictionary of {student: [grades]}; compute averages with loop, store in new dict, print top 3.

students = {
    "Mandar": [85, 90, 88],
    "Tejas": [70, 75, 72],
    "Yash": [95, 92, 96],
    "Nitesh": [60, 65, 58],
    "Maaz": [89, 91, 87]
}

# Compute averages
averages = {}
for s in students:
    total = 0
    for g in students[s]:
        total += g
    averages[s] = total / len(students[s])

# Find top 3 manually
for i in range(3):
    top_student = max(averages, key=averages.get)
    print(top_student, "->", round(averages[top_student], 2))
    del averages[top_student]

# Nested dict {class: {student: grades}}; function to find class average using recursion-like loops

classes = {
    "class A":{
        "Yash": [85, 90, 95],
        "Aniket": [75, 80, 80]
},
"classB":{
    "Vikas": [55, 60, 65],
    "Raj": [65, 70, 75]
}
}

def class_avgerage(data):
    class_avg = {}

    for class_name, student in data.items():
        total_marks = 0
        total_count = 0

        for grades in student.values():
            total_marks += sum(grades)
            total_count += len(grades)

        class_avg[class_name]= total_marks / total_count if total_count else 0
    return class_avg

result = class_avgerage(classes)
print(result)
        
# Function: Input list of tuples (id, score); sort by score descending using sorted() and loop.

def sort_by_score(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

    for item in sorted_data:
        print(item)

    return(sorted_data)

students = [(101, 85), (102, 92), (103, 78), (104, 90)]

result = sort_by_score(students)
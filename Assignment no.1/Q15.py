# Function to remove duplicates from list of dicts by key 'id' using set of ids.

def remove_dupli(direct_list):
    ids= set()                           # To store unique IDs
    unique_list = []

    for item in direct_list:
        if item["id"] not in ids:
            ids.add(item["id"])
            unique_list.append(item)
                               
    return unique_list

data = [
    {'id': 1, 'name': 'Mandar'},
    {'id': 2, 'name': 'Tajes'},
    {'id': 1, 'name': 'Yash'},
    {'id': 3, 'name': 'Raj'},
    {'id': 2, 'name': 'Nitesh'}
]

results = remove_dupli(data)
print (results)

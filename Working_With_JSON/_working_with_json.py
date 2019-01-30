import json


# Load JSON data from file
with open('json.txt') as file:
    data = json.load(file)
    for state in data:
        print(state)






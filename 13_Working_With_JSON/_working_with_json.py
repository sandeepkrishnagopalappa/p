import json

# Serialising dictionary to JSON file
profiles = {'profile': [
    {'fname': 'steve', 'lname': 'jobs'},
    {'fname': 'steve', 'lname': 'jobs'}
    ]
}

with open('profiles.json', 'w') as f:
    json.dump(profiles, f, indent=2)

# De-Serialising
# Load JSON data from file
with open('json.txt') as file:
    data = json.load(file)
    for state in data:
        print(state['name'], state['abbreviation'])

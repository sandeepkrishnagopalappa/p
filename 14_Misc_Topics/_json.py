# What is JSON?
"""
* JSON stands for **Java Script Object Notation**
* A standardised format commonly used for data transfer.
* Readable both of Humans and Machine.
* Used in Databases and API's.
* XML is one more format used for data transfer.

"""

info = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

"""
* Python has builtin module called `json` to help work with JSON data
# Serilisation and de-serilisation
* Encoding data into JSON format is called **serialisation**. e.x. Converting a python list to a JSON 
* Decoding JSON data is called **de-serilisation** e.x. Reading JSON data into Python Dictionary/List
"""

# Serialising data into JSON file.
# Let's consider a python dictionary
data = {
          "user": {
                     "name": "John Doe",
                     "age": 26
                  }
       }
"""
* The json module exposes two methods for serializing Python objects into JSON format
* **dump()** will write Python data to a file-like object. We use this when we want to serialize our Python data to an external JSON file.
* **dumps()** will write Python data to a string in JSON format. This is useful if we want to use the JSON elsewhere in our program, or if we just want to print it to the console to check that it’s correct.
"""
import json

with open('data.json', 'w') as f:
   json.dump(data, f, indent=4)

# Running above code creates a file named data.json, with python Dictionary converted into JSON format.

# To Serialise the above Python dictionary to string format.

import json

json.dumps(data, f, indent=4)

# de-serialising JSON data into Python Data-structure
import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

for user in users:
    print(user['email'], user['username'])

# Process the users data and Serialise into a JSON file.
import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

# Build a list of dictionaries with only "name" and "email" and serialise the data
data = [{"name": user['name'], "email": user['email']} for user in users]
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

import json
"""
Here we write Key value pairs as it is required for json format
"""
student = {
    'age': 25,
    'name': 'John',
    'year': 2025
}

file_path = 'jsonOutput.json'

try:
    with open(file_path, 'w') as file:
        json.dump(student, file, indent=4)
        print(f"Json file {file_path} was written successfully")
except Exception as err:
    print(f"Error occured, Reason: {err}")

import json

file_path = 'jsonOutput.json'

with open(file_path, 'r') as file:
    content = json.load(file)
    print(content['name'])

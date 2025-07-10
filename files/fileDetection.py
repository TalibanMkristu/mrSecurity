import os 

file_path = 'jsonOutput.json'

if os.path.exists(file_path):
    print(f"file path >> '{file_path}' does exist.")
    if os.path.isfile(file_path):
        print("This is a factor file")
    elif os.path.isdir(file_path):
        print("This is a direcory")
else:
    print("File path does not exists !")
    
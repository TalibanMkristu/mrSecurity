students = ['John', 'James', 'Peter']

file_path = 'txtOutput.txt'

try:
    with open(file_path, 'w') as file:
        for student in students:
            file.write(student + '\n')
        print('File written successfully')
except Exception as err:
    print(f"Error ocurred, Reason : {err}")
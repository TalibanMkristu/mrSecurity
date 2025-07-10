import csv

students = [
    ['name', 'age', 'job'],
    ['James', 30, 'prefect'],
    ['Peter', 28, 'classRep']
]

file_path = 'csvOutput.csv'
try:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)
        print("Csv file created successfully")

except Exception as err:
    print(f"Error occured,  Reason: {err}")

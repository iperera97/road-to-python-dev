import csv

def store_data_in_csv():
    csv_file = open("students.csv", "w", newline='')
    headers = ["id", "name", "age"]

    students_data = [
        {
            "id": 1,
            "name": "isuru",
            "age": 25
        },
        {
            "id": 2,
            "name": "mahesh",
            "age": 30
        }
    ]

    student_csv = csv.DictWriter(csv_file, headers)
    student_csv.writeheader()
    student_csv.writerows(students_data)

    csv_file.close()
    

store_data_in_csv()

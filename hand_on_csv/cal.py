import csv
import random


def store_data_in_csv(file_name, headers, data):
    csv_file = open(file_name, "w", newline='')

    csv_writer = csv.DictWriter(csv_file, headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)

    csv_file.close()

def read_data_in_csv(file_name):
    csv_file = open(file_name, 'r')
    data = csv.DictReader(csv_file)
    data = list(data)
    csv_file.close()
    return data

def generate_data():
    names = ["isuru", "john", "max", "kevin", "lin", "evin", "rock", "amal", "kamal", "zen"]
    ages = range(6, 19)
    years = range(2010, 2022)
    countries = ["sri lanka", "japan", "dubai"]

    data = []

    for index, val in enumerate(names):
        item = {
            "id": index + 1,
            "name": val,
            "age": random.choice(ages),
            "year": random.choice(years),
            "country": random.choice(countries),
        }
        data.append(item)
    
    store_data_in_csv("students.csv", ["id", "name", "age", "year", "country"], data)


def calculate_item_count(data):
    item_count = len(data)
    print(f"item_count {item_count}")

def calculate_min_max_age(data):
    total_ages = []

    for each in data:
        total_ages.append(
            int(each["age"])
        )

    max_age = max(total_ages)
    min_age = min(total_ages)

    print(f"maximum age {max_age}")
    print(f"minimum age {min_age}")
    return {
        "max": max_age,
        "min": min_age
    }

def filter_students_by_age(data, age):
    students = []

    for each in data:

        if int(each["age"]) == int(age):
            students.append(each)

    print(f"students on {age}")
    print(students)


def calculate_avg_on_age(data):
    ages = []

    for each in data:
        ages.append(int(each["age"]))

    avg = sum(ages) / len(data)
    print(f"avg {avg}")


def calculate_data():
    data = read_data_in_csv("students.csv")

    # check item count
    calculate_item_count(data)

    # check max age
    min_max = calculate_min_max_age(data)

    # get students with maximum age
    filter_students_by_age(data, min_max["min"])

    calculate_avg_on_age(data)


generate_data()
calculate_data()
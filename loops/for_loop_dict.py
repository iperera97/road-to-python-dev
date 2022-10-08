student = {
    "name": "john",
    "age": 25,
    "gender": "male",
    "email": "john@gmail.com"
}

# student values access
# print(student["name"])
# print(student["age"])
# print(student["gender"])

# loop dict
for key, value in student.items():
    print(f"{key} {value}")
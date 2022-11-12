class Student:
       
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_age(self):
        current_year = 2022
        age = current_year - self.birth_year
        print(f"age {age}")


# create object
s1 = Student("isuru", "mahesh", 1997)
print(s1.birth_year)
s1.calculate_age()

s2 = Student("john", "max", 2005)
print(s2.birth_year)
s2.calculate_age()
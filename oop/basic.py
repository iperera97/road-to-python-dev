# student class
# student object
# characters - name, age, gender (variables)
# behaviours - speek(), run(), walk() (functions)
# blueprint

class Student:
    
    # properties
    name = "isuru"
    age = 25
    gender = "male"

    # methods
    def speek(self):
        print("student can speek")

# create object
s1 = Student()

# access properties
print(s1.name)
print(s1.age)
print(s1.gender)

# access methods
s1.speek()    
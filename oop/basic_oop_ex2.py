class Student:

    class_code = 11 # class property

    def __init__(self, first_name, last_name): # magic method
        self.first_name = first_name # object property
        self.last_name = last_name # object property

    def __str__(self): # object method (magic method)
        return self.first_name

    @classmethod # class method
    def next_class_code(cls):
        return cls.class_code + 1

    def sayHello(self): # object method
        print(f"hello {self.first_name} {self.last_name}")

# object property / method - 
# class property / method - 

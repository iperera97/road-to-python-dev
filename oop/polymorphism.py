
class Cat:

    def make_sound(self):
        print("meow")


class Dog:

    def make_sound(self):
        print("bark")


c1 = Cat()
d1 = Dog()

for each in [c1, d1]:
    each.make_sound()

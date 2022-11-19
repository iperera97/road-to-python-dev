# employers - part time, full time, remote
# salary calculate = (hour * per_hour_amount) * 30

class BaseEmployer:

    def calculate_salary(self):
        return (self.hour * self.per_hour_amount) * 30


class PartTimeEmployer(BaseEmployer):

    per_hour_amount = 1000

    def __init__(self, hour):
        self.hour = hour 


class FullTimeEmployer(BaseEmployer):

    per_hour_amount = 1500

    def __init__(self, hour):
        self.hour = hour


p1 = PartTimeEmployer(4)
salary = p1.calculate_salary()
print("salary for part time", salary)

p2 = FullTimeEmployer(8)
salary = p2.calculate_salary()
print("salary for full time", salary)

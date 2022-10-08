numbers = [10, 20, 30, 40]
double_numbers = []

# normal loop
for num in numbers:
    double_numbers.append(num * 2)

# short hand loop
double_numbers = [num * 2 for num in numbers]
print(double_numbers)

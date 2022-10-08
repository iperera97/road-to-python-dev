numbers = [10, 20, 30, 40, 50, 60]
double_numbers = []

for num in numbers:

    if num == 30:
        continue

    if num == 50:
        break

    print(num)
    val = num * 2
    double_numbers.append(val)

print(double_numbers) # [20, 40, 80]
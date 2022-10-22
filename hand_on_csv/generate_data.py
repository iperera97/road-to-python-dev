data = []

for n in range(1, 3):
    print("enter your name")
    name = input()
    print("enter your age")
    age = input()

    data.append({
        "id": n,
        "name": name,
        "age": age    
    })

print(data)
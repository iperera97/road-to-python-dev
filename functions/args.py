def add(*values):
    val = 0

    for item in values:
        val += item
    
    return val

print(add(10, 20, 30)) # 60
print(add(100, 200, 300, 400, 500)) # 1500


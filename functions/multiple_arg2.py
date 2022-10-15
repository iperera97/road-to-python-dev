def total(data1, data2, data3):
    v1 = 0
    for item in data1:
        v1 += item

    v2 = 0
    for item in data2:
        v2 += item

    v3 = 0
    for item in data3:
        v3 += item

    return v1, v2, v3


input1 = [10, 20, 30]
input2 = [200, 300]
input3 = [1000, 2000, 3000]

result = total(input1, input2, input3)
print(result[0])
print(result[1])
print(result[2])

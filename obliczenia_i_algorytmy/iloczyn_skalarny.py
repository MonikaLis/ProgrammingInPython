import math

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
result = []

for i in range(len(a)):
    res = a[i] + b[i]
    result.append(res)

for i in result:
    print("result:{}".format(i))



import random
n = int(input("Hay nhap so phan tu:"))
array = []
for item in range(n):
    a = float(random.uniform(0,99))
    array.append(a)
print(array)
min = array[0]
for item in array:
    if item < min:
        min = item
print("Min la: ", min)
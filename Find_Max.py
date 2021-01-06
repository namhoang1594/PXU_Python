import random
n = int(input("Hay nhap so phan tu: "))
array = random.sample(range(0,99),n)
max = array[0]
for item in array:
    if max < item:
        max = item
print (array)
print ('Max la: ',max)
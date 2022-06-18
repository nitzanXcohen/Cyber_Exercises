#Ex1: Python Starter and Numeric Bases
#1 -
num = input("type a number")
try:
    dec = int(num, 16)
    print(dec)
except ValueError:
    print("invalid hex number")

#2 -
num = input("type a string")
i, sum, temp = 0, 0, -1

for x in range(0, len(num)):
    try:
         int(num[x], 16)
    except ValueError:
        sum += int(num[temp+1:x], 16)
        temp = x
try:
    sum += int(num[temp+1:len(num)], 16)
except ValueError:
    sum = sum

print(sum)

#3 -
num = int(input("type number"))
counter, sum = 1, num
try:
    while num == num:
        num = int(input("type number"))
        sum += num
        counter += 1
except ValueError:
    print(sum/counter)

def factorial(num):
   if num == 1:
       return num
   else:
       return num*factorial(num-1)
num = int(input("type num"))
print("number - ", num ," factorial = ", factorial(num))


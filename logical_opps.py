# A simple calculator app

print('''---------------------------------------------------------
1. Addition
2. Subtraction 
3. Multiplication
4. Division
5. Exponential									-------------------------------------------------------------- ''')

print("Enter two numbers to add:")
#prompt a user for a number and save it
first_n = input("first number:")
#prompt a user for a number and save it
second_n = input("second number:")
sum =float(first_n) + float(second_n)
print(f"{first_n} + {second_n} = {sum:.2f}")

print("Enter two numbers to sub:")
#prompt a user for a number and save it
first_n = input("first number:")
#prompt a user for a number and save it
second_n = input("second number:")
sum =float(first_n) - float(second_n)
print(f"{first_n} - {second_n} = {sum:.2f}")

#multiplication
print("Enter two numbers to mul:")
#prompt a user for a number and save it
first_n = input("first number:")
#prompt a user for a number and save it
second_n = input("second number:")
sum =float(first_n) * float(second_n)
print(f"{first_n} * {second_n} = {sum}:.2f")

#division
print("Enter two numbers to divide:")
#prompt a user for a number and save it
first_n = input("first number:")
#prompt a user for a number and save it
second_n = input("second number:")
sum =float(first_n) / float(second_n)
print(f"{first_n} / {second_n} = {sum:.2f}")

#exponent
print("Enter two numbers to exponent:")
#prompt a user for a number and save it
first_n = input("first number:")
#prompt a user for a number and save it
second_n = input("second number:")
sum =float(first_n) ** float(second_n)
print(f"{first_n} ** {second_n} = {sum:.2f}")


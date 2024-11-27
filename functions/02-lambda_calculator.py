gathering_num = lambda a, b: a + b
subtraction_num = lambda a, b: a - b
multiply_num = lambda a, b: a * b
devide_num = lambda a, b: a / b

a = float(input())
b = float(input())
operator = input()

if operator == "+":
    print(gathering_num(a, b))
elif operator == "-":
    print(subtraction_num(a, b))
elif operator == "*":
    print(multiply_num(a, b))
elif operator == "/":
    if b == 0:
        print("You can`t divide by ZERO")
    else:
        print(devide_num(a, b))

#Съжалявам че не е като в изискването
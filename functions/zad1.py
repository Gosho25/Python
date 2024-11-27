def povdigane(num1, num2):
    power = num1 ** num2
    return power
number1, number2 = [int(x) for x in input().split(", ")]

print(f"{number1} to the power {number2} is: ")
print(povdigane(number1, number2))

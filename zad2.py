def string_to_number(string):
    try:
        number = float(string)
        return number
    except ValueError:
        print(f'"{string}" is not number')

string1 = "123.45"
num1 = string_to_number(string1)
print(f'"{string1}"={num1}')

string2 = "abc"
num2 = string_to_number(string2)
print(f'"{string2}"= {num2}')
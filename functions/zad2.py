from math import sqrt
def find_sqrt(my_list):
    sqrt_list = []
    for num in my_list:
        kvadr = math.sqrt(num)
        sqrt_list.append(kvadr)
    return sqrt_list

iput = input()
list = [float(num) for num in iput.split(", ")]
result = find_sqrt(list)
print(result)
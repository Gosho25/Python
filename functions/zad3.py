def input_numbers():
    rl_numbers = float(input())
    list = []

    for i in range(rl_numbers):
        num = float(input({i+1}))
        list.append(num)

    real_stojnost = list(map(lambda x: abs(x), list))

    return real_stojnost

result = input_numbers()
print(result)
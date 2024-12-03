from data_operations import save_to_file, read_from_file, push, pop

def process_data():
    numbers = [1, 2, 3, 4, 5]
    stack = []
    for num in numbers:
        push(stack, num)
    total_sum = 0 
    while len(stack) > 0:
        total_sum += pop(stack)

    result = "Sum of the numbers is: {}\n".format(total_sum)
    result += "The numbers are: {}".format(numbers)
    
    save_to_file("result.txt", result)

    file_content = read_from_file("result.txt")
    if file_content:
        print(file_content)

    if __name__ == "main2":
        try:
            process_data
        except Exception as e:
            print("Error by the time to run: ", e)
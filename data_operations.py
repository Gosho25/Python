def save_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except:
        print("Error with saving")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except:
        print("Error with reading")
        return None
    

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        print("Error: The stack is empty")
        return None
    return stack.pop()
    
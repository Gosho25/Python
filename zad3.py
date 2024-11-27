with open('log.txt', 'r') as l:
    lines = l.readlines()
    error_count = 0
    for line in lines:
        if "error" in line.lower():
            error_count += 1          
    print(f"{error_count}")            
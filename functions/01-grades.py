def assessment(assesment):
    assessment = float(input())
    for assesment in range(2.00, 6.00):
        if assesment <= 2.99:
            print("Fail")
        elif assesment  >= 3.00 or  3.49:
            print("Poor")
        elif assesment >= 3.50 or 4.49:
            print("Good")
        elif assesment >= 4.50 or 5.49:
            print("Very Good")
        elif assesment >= 5.50 or 6.00:
            print("Excellent")



print(assessment)
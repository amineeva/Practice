# print a pyramid pattern with adding numbers

def pyramid_pattern(number):
    for i in range(number):
        for count in range(i+1):
            print(i+1, end=" ")
        print("\n")

pyramid_pattern(5)
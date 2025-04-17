# get each digit from a number in reverse order

def reverse_int(number):
    for i in range(len(str(number))):
        print(str(number)[-1-i], end =" ")

reverse_int(7536)
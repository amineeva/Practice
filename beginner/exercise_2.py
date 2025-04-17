# print sum of current number and previous number

def adding_current_and_previous(number_range):
    prev_number = 0
    for i in range(number_range):
        if i==0:
            prev_number = 0
        else:
            prev_number = i-1
        sum = prev_number+i
        print(f"Current Number", i, "Previous Number", prev_number, "Sum:", sum)

adding_current_and_previous(10)
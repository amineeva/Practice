# Check if first and last numbers of list are the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 36, 75, 30]

def first_last_match_list(list):
    first_value = list[0]
    last_value = list[len(list)-1]
    if first_value==last_value:
        print("result is True")
    else:
        print("result is False")

first_last_match_list(numbers_x)
first_last_match_list(numbers_y)
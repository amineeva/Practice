# Display numbers divisible by 5

def only_divisible_by_5(list):
    for i in range(len(list)):
        if(list[i]%5==0):
            print(list[i])

only_divisible_by_5([10, 20, 33, 46, 55])
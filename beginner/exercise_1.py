# Calculate the multiplication and sum of two numbers

def multiplication_or_sum(number1, number2):
    if number1*number2 <= 1000:
        print(f"The result is", number1*number2)
    else:
        print(f"The result is", number1+number2)

multiplication_or_sum(20, 30)
multiplication_or_sum(40, 30)

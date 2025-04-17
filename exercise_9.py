# Check if a number is a palindrome

def check_palindrome(number):
    print(f"original number", number)
    print_out = ""
    for i in range(len(str(number))):
        # check each value backwards
        if(str(number)[i]==str(number)[i*-1 -1 ]):
            print_out = "Yes. given number is a palindrome number"
        else:
            print("No. given number is not a palindrome number")
            return None
    print(print_out)


check_palindrome(121)
check_palindrome(125)
# Print characters present at an even index number

def print_only_even_index():
    word = input("Enter word: ")
    print(f"Original String is", word)
    print("Printing only even index chars")
    for i in range(len(word)):
        if i%2==0:
            print(word[i])

print_only_even_index()
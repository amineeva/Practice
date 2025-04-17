# Remove first n characters from a string

def remove_chars(word, number):
    return word[number:len(word)] #OR word[number:]

print(remove_chars("PYnative", 2))
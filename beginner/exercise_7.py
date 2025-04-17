# find number of occurences of a substring in a string

str_x = "Emma is a good developer. Emma is a writer."

def substring_counter(main_string, substring):
    count = main_string.count(substring)
    print(f"",substring,"appeared", count, "times")

substring_counter(str_x, "Emma")
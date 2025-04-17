# print multiplication table from 1 to 10

def print_multiplication_table(rows, columns):
    for r in range(rows):
        for c in range(columns):
            print((r+1)*(c+1), end = " ")
        print("\n")

print_multiplication_table(10, 10)


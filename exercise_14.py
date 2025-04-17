# downward half-pyramid star pattern

def downward_half_pyramid(rows):
    for i in reversed(range(rows)):
        for row_print in range(i+1):
            print("*", end ="")
        print("\n")



downward_half_pyramid(5)
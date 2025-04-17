# Merge two lists, odd from first, even from second

def merge_list(list_1, list_2):
    list_final = []
    for i in range(len(list_1)):
        if list_1[i] % 2 == 1:
            list_final.append(list_1[i])
    for i in range(len(list_2)):
        if list_2[i] % 2 == 0:
            list_final.append(list_2[i])

    print(f"result list:", list_final)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

merge_list(list1, list2)
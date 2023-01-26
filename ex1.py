try:
    import random
    length = int(input("Enter the number of items in the lists: "))
    choice = int(input("1) Items in both lists \n 2) Elements of both lists without repetition \n 3) Elements common to both lists \n 4) Only unique elements of each list \n 5) minimum and maximum values of each of the lists \n Enter your choice:"))
    list1 = []
    list2 = []

    if length > 0:
        for i in range(length):
            list1.append(random.randint(0, 100))
            list2.append(random.randint(0, 100))

    print("List 1: ", list1)
    print("List 2: ", list2)

    if choice == 1:
        list3 = list1 + list2
        print("Items in both lists: ", list3)

    if choice == 2:
        list3 = list(set(list1 + list2))
        print("Items in both lists without duplicates: ", list3)

    if choice == 3:
        list3 = list(set(list1) & set(list2))
        print("Elements common to both lists: ", list3)

    if choice == 4:
        list3 = list(set(list1) ^ set(list2))
        print("Only unique elements of each list: ", list3)

    if choice == 5:
        list3 = min(list1), max(list1)
        list4 = min(list2), max(list2)
        print("Minimum and maximum 1 list: ", list3)
        print("Minimum and maximum 2 list: ", list4)
    else:
        print("Items in the lists must be positive")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')


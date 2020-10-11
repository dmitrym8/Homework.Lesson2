words_by_user = input("please enter any number of words divided by the space: ")
list = words_by_user.split(" ")
print(list)

i = 0
for el in list:
    print(f"row #{i+1}: {list[i][:10]}")
    i += 1



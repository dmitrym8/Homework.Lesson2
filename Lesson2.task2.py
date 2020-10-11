len_of_list = int(input("please enter the length of the list: "))

while len_of_list <= 0:
    print("integer figure above zero")
    len_of_list = int(input("please enter the length of the list: "))

my_list = []
i = 0
while i < len_of_list:
    my_list.append(input(f"enter element number '{i+1}': "))
    i = i + 1

print(f"initial list: {my_list}")

i = 0
while i <= len(my_list) - 1:
    temp = my_list[i]
    my_list.pop(i)
    my_list.insert(i+1, temp)
    i = i + 2
print(f"updated list: {my_list}")


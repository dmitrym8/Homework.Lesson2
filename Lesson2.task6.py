my_dict = {}
my_tuple = ()
my_list = []
item_number = 0

while item_number < 3:
    type_of_device = input("enter type of device: ")
    price = int(input("enter the price of device: "))
    number_of_devices = int(input("enter number of devices: "))
    type_of_count = input("enter type of count: ")
    item_number += 1
    new_dict = {"name of device": type_of_device, "price": price, "number of devices": number_of_devices, "type of count": type_of_count}
    new_tuple = (item_number, new_dict)
    my_list.extend(new_tuple)

print(*my_list, sep = "\n")

#сделал первую часть задачи - собрал структуру товаров



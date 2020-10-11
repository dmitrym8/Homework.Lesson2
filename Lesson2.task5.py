my_rating = []

while len(my_rating) < 100: #формальное ограничение, чтобы не допускать бесконечность
    add_number = int(input("please enter a number: "))
    my_rating.append(add_number)
    my_rating.sort()
    my_rating.reverse()
    print(my_rating)

my_dict_months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
my_dict_seasons = {'Jan': 'Winter', 'Feb': 'Winter', 'Mar': 'Spring', 'Apr': 'Spring', 'May': 'Spring', 'Jun': 'Summer', 'Jul': 'Summer', 'Aug': 'Summer', 'Sep': 'Autumn', 'Oct': 'Autumn', 'Nov': 'Autumn', 'Dec': 'Winter'}
list_of_months_for_user = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

selected_month = int(input(f"please input the months number out of the list: {list_of_months_for_user}: "))
selected_month = (my_dict_months.get(selected_month))
print(my_dict_seasons.get(selected_month))

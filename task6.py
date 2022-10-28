list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

length = len(list_numbers)
id_last=length-1
max_var = [max(list_numbers), list_numbers.index(max(list_numbers))]
last_var = [list_numbers[id_last], id_last]
list_numbers[max_var[1]] = last_var[0]
list_numbers[last_var[1]]=max_var[0]

print(list_numbers)


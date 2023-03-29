


def insertion_sort(tuple_to_sort):
	list_to_sort = list(tuple_to_sort)
	count = 0
	while count < len(tuple_to_sort):
		found = False
		current = count
		while found == False:
			if list_to_sort[current] < list_to_sort[current - 1] and current >= 1:
				temp = list_to_sort[current]
				list_to_sort[current] = list_to_sort[current - 1]
				list_to_sort[current - 1] = temp
				current -= 1
			else:
				found = True
				count += 1
	return list_to_sort








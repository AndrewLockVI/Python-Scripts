
def default_sort(tuple_to_sort):
	list_to_sort = list(tuple_to_sort)
	list_to_sort.sort()
	return list_to_sort

if __name__ == '__main__':
	print(default_sort((10 , 15, 20, 2, 2)))


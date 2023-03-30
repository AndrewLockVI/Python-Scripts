def selection_sort(sort_list):
    sort_list = sort_list.copy()
    smallest_val = sort_list[0]
    sorted_list = []
    smallest_index = 0
    length = len(sort_list)
    x = 0
    while x < length - 1:
        count = 0
        for i in sort_list:
            if i < smallest_val:
                smallest_val = i
                smallest_index = count
            count += 1
        sort_list.pop(smallest_index)
        sorted_list.append(smallest_val)
        x += 1
        smallest_val = sort_list[0]
        smallest_index = 0
    #This adds on the last value because it can't be compared to any other
    #Values it would make the above function error out.
    sorted_list.append(sort_list[0])
    return sorted_list


def count_sort(sort_list):
    
    count = 0
    highest_val = 0
    lowest_val = sort_list[0]

    # This finds the highest and lowest values in the list
    while count < len(sort_list):
        if sort_list[count] > highest_val:
            highest_val = sort_list[count]
        if sort_list[count] < lowest_val:
            lowest_val = sort_list[count]
        count += 1

    #This then uses the highest and lowest values to find the range which
    #will be used to add one to the value in the temp_list at the proper index

    integer_range = (highest_val + 1) - lowest_val
    temp_list = [0] * integer_range
    count = 0

    while count < len(sort_list): 
        item_val = sort_list[count] - lowest_val
        temp_list[item_val] = temp_list[item_val] + 1
        count += 1

    #This uses the temp_list to create a new list with all of the elements sorted

    count = 0
    return_list = []
    while count < len(temp_list):
        for i in range(0, temp_list[count]):
            return_list.append(lowest_val + count)
        count += 1
    return return_list



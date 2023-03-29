import sys
import random
import time














def selection_sort(tuple_to_sort):
    smallest_val = tuple_to_sort[0]
    sort_list = list(tuple_to_sort)
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




def random_list(length):
    count = 0
    list_to_sort = []
    while count < length:
        count += 1
        list_to_sort.append(int(100 * random.random()))
    return list_to_sort

def random_list_change(sort_list):

    sorted_list = []
    length = len(sort_list)
    sort_list = list(sort_list)

    while len(sort_list) > 0:
        rnd_val = random.randint(0, len(sort_list) - 1)
        sorted_list.append(sort_list[rnd_val])
        sort_list.pop(rnd_val)
    
    return sorted_list

def random_sort(sort_list):
    
    sort_tuple = tuple(sort_list)

    sorted = False
    iterations = 0
    while sorted == False:
        
        sorted_tuple = tuple(random_list_change(sort_tuple))

        sorted = True
        count = 0
        while count < len(sorted_tuple) - 1:
            if sorted_tuple[count] > sorted_tuple[count + 1]:
               sorted = False
            count += 1
        iterations += 1
    print(f'Iterations Done: {iterations}')
    return list(sorted_tuple)

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

if __name__ == '__main__':
    try:
        list_length = int(sys.argv[1])
    except:
        list_length = int(input("How long would you like the list to be: "))
    try:
        sort = sys.argv[2]
    except:
        sort = 'all'

    list_to_sort = []
    list_to_sort = random_list(list_length)
    
    #This times how long the count sort takes
    
    if sort == 'count' or sort == 'all':
        t0 = time.time()
        sorted_list = count_sort(list_to_sort)
        t1 = time.time()
        count_time = t1 - t0
        print("Count Sort Time: " + str(count_time))

    if sort == 'random' or sort == 'all':
        t0 = time.time()
        sorted_list = random_sort(tuple(list_to_sort))
        t1 = time.time()
        random_time = t1 - t0
        print("Random Sort Time: " + str(random_time))

    if sort == 'selection' or sort == 'all':
        t0 = time.time()
        sorted_list = selection_sort(tuple(list_to_sort))
        t1 = time.time()
        selection_time = t1 - t0
        print("Selection Sort Time: " + str(selection_time))
    

    try:
        print(sorted_list)
    except:
        print('Invalid option please input an integer then a sort type. Leave type blank for all.')

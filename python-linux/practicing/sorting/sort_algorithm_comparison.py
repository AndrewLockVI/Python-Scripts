import sys
import random
import time
from selection_sort import selection_sort
from random_sort import random_sort
from count_sort import count_sort
from default_sort import default_sort
from insertion_sort import insertion_sort
from average_sort import average_sort












def random_list(length):
    count = 0
    list_to_sort = []
    while count < length:
        count += 1
        list_to_sort.append(int(random.random()* 100))
    return list_to_sort



if __name__ == '__main__':
    try:
        list_length = int(sys.argv[1])
    except:
        list_length = int(input("How long would you like the list to be: "))
    try:
        do_stupid_sorts = sys.argv[2]
    except:
        do_stupid_sorts = 'f'

    list_to_sort = []
    list_to_sort = random_list(list_length)
    
    
    t0 = time.time()
    sorted_list = count_sort(list_to_sort)
    t1 = time.time()
    count_time = t1 - t0
    print("Count Sort Time: " + str(count_time))

    if do_stupid_sorts != 'f':
        t0 = time.time()
        sorted_list = random_sort(list_to_sort)
        t1 = time.time()
        random_time = t1 - t0
        print("Random Sort Time: " + str(random_time))
	
    t0 = time.time()
    sorted_list = selection_sort(list_to_sort)
    t1 = time.time()
    selection_time = t1 - t0
    print("Selection Sort Time: " + str(selection_time))            
    t0 = time.time()	
    sorted_list = default_sort(list_to_sort)
    t1 =  time.time()
    default_time = t1 - t0
    print("Default Sort Time: " + str(default_time))

    t0 = time.time()
    sorted_list = insertion_sort(list_to_sort)
    t1 = time.time()
    insertion_time = t1 - t0
    print("Insertion Time: " + str(insertion_time))


    t0 = time.time()
    sorted_list = average_sort(list_to_sort)
    t1 = time.time()
    average_time = t1 - t0
    print("Average Sort Time: " + str(average_time))



    if len(sorted_list) < 15:
        print(sorted_list)

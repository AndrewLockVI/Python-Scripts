import threading
import time
import importlib
import sort_algorithm_comparison as sac

def sleep_sort(input_num):
    input_num = int(input_num)
    time.sleep(input_num)
    print(input_num)


if __name__ == '__main__':
    long_list = sac.random_list(10)
    print(long_list) 
    for i in long_list:
        threading.Thread(target = sleep_sort, args=(i,)).start()
     

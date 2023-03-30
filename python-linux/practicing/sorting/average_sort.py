from insertion_sort import insertion_sort

#Something I just randomly came up with that first sorts
#the data by greater then or less then the mean
#then is runs insertion sort. I thought this 
#might be faster than standard insertion sort because
#insertion sort is generally faster when you have partially
#sorted lists.

def average_sort(sort_list):
    total_num = 0
    average_num = 0
    for i in sort_list:
        total_num += i
    average_num = float(total_num) / float(len(sort_list))
    print(average_num)
    
    count = 0
    new_list = []
    for i in sort_list:
        if(float(sort_list[count]) > float(average_num)):
            new_list.append(i)
        else:
           new_list.insert(0 , i)

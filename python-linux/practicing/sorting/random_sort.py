import random
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

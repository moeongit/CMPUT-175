import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

def min_index(data, first, last):
    if first == last:
        return first
    i = min_index(data, first + 1, last) 
    if data[first] > data[i]:
        return first
    else:
        return i

def recursive_selection_sort(data, data_len, index = 0): 
    if index == data_len: 
        return -1    
    temp = min_index(data, index, data_len - 1)
    if temp != index: 
        data[temp], data[index] = data[index], data[temp] 
    recursive_selection_sort(data, data_len, index + 1)
#---------------------------------------#
#Implement the Recursive merge sort here
def recursive_merge_sort(data): 
    data_len = len(data)
    if len(data) <= 1:
        return data

    mid = data_len // 2
    left_list = data[:mid]
    right_list = data[mid:]

    recursive_merge_sort(left_list)
    recursive_merge_sort(right_list)
    i, j, k = 0, 0, 0   

    size_of_left = len(left_list)
    size_of_right = len(right_list)

    while i < size_of_left and j < size_of_right:
        if left_list[i] >= right_list[j]:
            data[k] = left_list[i]
            i += 1
        else:
            data[k] = right_list[j]
            j += 1
        k += 1
    while i < size_of_left:
        data[k] = left_list[i]
        i += 1
        k += 1
    while j < size_of_right:
        data[k] = right_list[j]
        k += 1
        j += 1
    while i < size_of_left and j < size_of_right:
        if left_list[i] <= right_list[j]:
                data[k] = left_list[i]
                i += 1
        else:
            data[k] = right_list[j]
            j += 1
            k += 1

        while i < size_of_left:
            data[k] = left_list[i]
            i += 1
            k += 1

        while j < size_of_right:
            data[k] = right_list[j]
            j += 1
            k += 1
    return data
        
data = [1, 5, 3, 4, 6, 8, 7, 2]
recursive_merge_sort(data)
print(data)
#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
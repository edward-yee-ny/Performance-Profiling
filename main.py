import timeit
import random
n = 1
length = 10

def test() -> int:
    """Test the performance of linear search on 1000 elements"""
    data = list(range(1000))
    data = random.shuffle(data)
    target = 777
    for i, value in enumerate(data):
        if value == target:
            # index found
            return i

# # Note that the function should be passed to `timeit.timeit` without '()'
# # We don't want to call the function, instead we pass it to timeit.
# # timeit will call the function (without arguments) and measure the time taken.
# time taken code --> timeit.timeit(test, number=n)


def bubble_sort() -> list:
    """
    Sorts a list via bubble sort algorithm
    """
    data = list(range(length))
    random.shuffle(data)
    for n in range(len(data)):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp    
    return data


def insertion_sort():
    """
    Sorts a list via insertion sort algorithm
    """
    data = list(range(length))
    random.shuffle(data)
    #Assume first element is sorted
    for i in range(len(data)):
    
        target = data[i]
        j = i - 1
        while j > 0 and data[j] > target:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = target
                
    
    return data





def merge(left, right):
    """
    Merge!
    """
    merged_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))

    return merged_list + left + right

def merge_sort(data):
    if len(data) <= 1:
        return data
    # Split the array into two halves
    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def quicksort(data):
    if len(data) <= 1:
        return data
    less = []
    more = []
    pivot = data.pop()
    for i in data:
        if i <= pivot:
            less.append(i)
        else:
            more.append(i)
    left = quicksort(less)
    right = quicksort(more)
    return left + [pivot] + right

def binary_search()
# ####bubblesort####
# print("bubble sort")
# bblsort = []
# for i in range(6):
#     length *= 3
#     bblsort.append([timeit.timeit(bubble_sort, number = n),length])# we need to analyse the data so dont add unecessary text
#     print(bblsort[i])

# ###insertion sort###
# length = 10
# print("insertion sort")
# insert_sort = []
# for i in range(7):
#     length *= 3
#     insert_sort.append([timeit.timeit(insertion_sort, number = n), length])
#     print(insert_sort[i])

###merge sort###
# length = 10
# print("merge sort")
# merg_sort = []
# # print(merge_sort([5, 7, 3]))
# for i in range(7):
#     length *= 5
#     data = list(range(length))
#     random.shuffle(data)
#     merg_sort.append([timeit.timeit(lambda: merge_sort(data), number = n),length])
#     print(merg_sort[i])

##quick sort###
length = 10
print("quick sort")
quic_sort = []
# print(merge_sort([5, 7, 3]))
for i in range(7):
    length *= 5
    data = list(range(length))
    random.shuffle(data)
    quic_sort.append([timeit.timeit(lambda: quicksort(data), number = n),length])
    print(quic_sort[i])
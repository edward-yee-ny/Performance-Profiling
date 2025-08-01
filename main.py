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
    leftidx = 0
    rightidx = 0
    for i in range(len(left) + len(right)):
        if (not( leftidx == len(left))) and (not (rightidx == len(right))):
            if left[leftidx] < right[rightidx]:
                merged_list.append(left[leftidx])
                leftidx += 1
            else:
                merged_list.append(right[rightidx])
                rightidx += 1
        else:
            merged_list += right[rightidx:]
            merged_list += left[leftidx:]
    return merged_list

def merge_sort(data):
    if len(data) <= 1:
        return data

    # Split the array into two halves
    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def callmerge():
    data = list(range(length))
    random.shuffle(data)
    merge_sort(data)
    return data



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
length = 10
print("merge sort")
merg_sort = []
for i in range(7):
    length *= 3
    merg_sort.append([timeit.timeit(callmerge(), number = n), length])
    print(merg_sort[i])
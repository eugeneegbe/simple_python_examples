# Write a function to reverse an array in-place (without creating a new array).
# Analyze its time and space complexity

def reverse_array(arr):

    i = 0
    j = len(arr) - 1
    mid = j / 2

    while i < mid:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j-=1
    return my_list

my_list = [1, 2, 3, 4, 3, 14, 15]
print(reverse_array(my_list))


# -> final result = [15, 14, 3, 4, 3, 2, 1]
# Take note of the middle element len(arr) / 2
# Note the temp isused to hold one value for it not ot repeat
# take to ierators i and j = len(arr) - 1 
# check if |i| == |j| == middle -> stop 
# count i upwards and j downwards

# Note: The complexity of such and implementation is O(n)
# as we have to go through the a maximum of N elements to do the swap


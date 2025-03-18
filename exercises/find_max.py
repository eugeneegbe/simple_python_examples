# Python function to find the maximum element in an arry

def find_max(arr):
    if not arr:
        return None
    max = arr[0]
    for element in arr:
        if element > max:
            max = element
    
    return max


array = [-3, -32, 2, -1, 4]
print(find_max(array))

# let the first element be the first
# walk through finding which is bigger than it and update the new max
# Note: This algorithm is O(n) as we iterate over the arry n/2 times

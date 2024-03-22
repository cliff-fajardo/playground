# sorted array
# arr = List
# key = target value

def binSearch(arr, key):
    left = 0
    right = len(arr)-1

    while left < right:                 # go through array until left and right pointer don't intersect
        mid = (left + right) // 2       # find the midpoint
        if arr[mid] == key:
            return mid                  # return the index
        elif key < arr[mid]:
            right = mid - 1             # move right index over to mid - 1
        else:
            left = mid + 1              # move left index over to mid + 1

    return -1





arr = [5, 12, 18, 22, 35, 28, 99, 125]
key = 2

print(binSearch(arr,key))
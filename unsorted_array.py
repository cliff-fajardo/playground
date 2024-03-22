# arr = List
# target = target value
# unsorted array
# return two numbers that when added, are equal to the target

def findTargetPair(arr, target):
    comp_set = set()                        # initialize a set to store already visited values

    for i in range(len(arr)):               # loop through an array
        compliment = target - arr[i]        # compliment is the number + arr value to equal target
        if compliment in comp_set:          # check the set if the compliment exists in the set
            return [compliment, arr[i]]     # return the pair
        else:
            comp_set.add(arr[i])            # add the visited value in the set



arr = [5, 100, 25, 21, 3, 22]
target = 122
print(findTargetPair(arr, target))
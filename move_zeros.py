

def moveZeroes(nums):
    l, r = 0, 1

    while r < len(nums):
        if nums[l] == 0:
            if nums[r] != 0:
                temp = nums[r]
                nums[l] = nums[r]
                nums[r] = temp
            else:
                r += 1










nums = [0,1,0,3,12]  # output: [1,3,12,0,0]
moveZeroes(nums)
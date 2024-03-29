# arr - array of price
# return the maximum profit

def maxProfit(arr):
    if len(arr) < 2:
        return 0

    b = 0       # buy index
    s = 1       # sell index
    maxP = 0    # keep track of max profit

    while s < len(arr):                 # iterate through array from left to right

        if arr[b] < arr[s]:             # check if buy price is less than sell price
            profit = arr[s] - arr[b]    # calculate the profit
            maxP = max(profit, maxP)    # store the max profit
        else:
            b = s                       # sell point is lower than buy, so move buy to sell point
        s += 1                          # move sell point to the next space
    return maxP




arr = [8,9, 34, 2]
print(maxProfit(arr))


# Factorial: n! = (n-0) * (n-1) * (n-2) ...
# Ex: 5! = (5) * (4) * (3) * (2) * (1) = 120

# iterative generally has less time and space complexity
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# recursion needs O(n) space complexity
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]             # substring of string from 0 to i
            back = string[i+1:]             # substring of string from after i to end
            together = front + back
            permute(together, letter + pocket)




print(iterative_factorial(5))
print(recur_factorial(5))

permute('test')

s = 'space'
print(s[0:0])
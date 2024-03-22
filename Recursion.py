

# Factorial: n! = (n-0) * (n-1) * (n-2) ...
# Ex: 5! = (5) * (4) * (3) * (2) * (1) = 120


def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


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
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)




print(iterative_factorial(5))
print(recur_factorial(5))

from matplotlib.pyplot import grid


def gridTraveler(m, n, memo={}):
    # check if arguments in memo
    if(frozenset([m, n]) in memo):
        return memo[frozenset([m, n])]

    if(m == 1 and n == 1):
        return 1
    if(m == 0 or n == 0):
        return 0

    memo[frozenset([m, n])] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return memo[frozenset([m, n])]


print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(18, 18))

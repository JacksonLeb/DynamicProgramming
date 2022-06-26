def canSum(target, numbers, memo={}):
    if(target in memo):
        return memo[target]

    if(target == 0):
        return True

    if(target < 0):
        return False

    for num in numbers:
        remainder = target - num
        if(canSum(remainder, numbers) == True):
            memo[target] = True
            return True

    memo[target] = False
    return False


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))

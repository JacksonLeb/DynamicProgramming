from pickle import NONE


def howSum(targetSum, numbers, memo={}):
    print(memo)
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return []
    if(targetSum < 0):
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)

        if(remainderResult != None):
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]
    memo[targetSum] = None
    return None


print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(300, [7, 14]))

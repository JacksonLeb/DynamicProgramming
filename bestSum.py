def bestSum(targetSum, numbers, memo={}):
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return []
    if(targetSum < 0):
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)

        if(remainderCombination != None):
            combination = [*remainderCombination, num]
            if(shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))

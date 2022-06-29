def howSum(targetSum, numbers):
    table = []
    for num in range(targetSum):
        table.append(None)
    table[0] = []

    for i in range(targetSum):
        if(table[i] != None):
            for num in numbers:
                if(i + num < targetSum):
                    table[i + num] = [*table[i], num]

    return table[targetSum - 1]


print(howSum(7, [5, 3, 4, 7]))

def bestSum(targetSum, numbers):
    table = []
    for i in range(targetSum):
        table.append(None)

    table[0] = []
    for i in range(targetSum):
        if(table[i] != None):
            for num in numbers:
                if(table[i + num] != None):
                    combo = [*table[i], num]
                    if(len(table[i + num]) > len(combo)):
                        table[i + num] = combo
    print(table)
    return table[targetSum - 1]


print(bestSum(8, [2, 3, 5]))

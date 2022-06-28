def canSum(targetSum, numbers):
    table = []
    for x in range(targetSum + 1):
        table.append(False)

    table[0] = True

    for i in range(targetSum):
        if(table[i] == True):
            for num in numbers:
                if((i + num) <= targetSum):
                    table[i + num] = True
    print(table)
    return table[targetSum]


print(canSum(7, [2, 4]))

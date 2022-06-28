def gridTraveler(m, n):
    # length and columsn m+1, n+1
    table = []
    for i in range(m+1):
        newArray = []
        for x in range(n+1):
            newArray.append(0)
        table.append(newArray)

    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            curr = table[i][j]
            if(j + 1 <= n):
                table[i][j + 1] += curr
            if(i + 1 <= m):
                table[i + 1][j] += curr
    return table[m][n]


print(gridTraveler(3, 2))
print(gridTraveler(18, 18))

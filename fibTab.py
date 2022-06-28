def fib(n):
    table = []
    for i in range(n + 1):
        table.append(0)

    table[1] = 1
    print(table)
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    print(table)
    return table[n]


print(fib(6))

n, m = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = []

for column_index in range(m):
    column_sum = 0
    for row_index in range(n):
        column_sum += matrix[row_index][column_index]
    result.append(column_sum)

[print(x) for x in result]

matrix = eval(input("Please enter a matrix: "))
coloumn = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    coloumn.append(row)

print(coloumn)
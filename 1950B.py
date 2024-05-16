t = int(input())
while t > 0:
    n = int(input())
    rowSize = n * 2
    colSize = n * 2
    row = 0
    col = 0
    arr = [['' for _ in range(colSize)] for _ in range(rowSize)]
    turn = '#'
    while row < rowSize:
        start = turn
        while col < colSize:
            if start == '#':
                arr[row][col] = '#'
                arr[row][col + 1] = '#'
                arr[row + 1][col] = '#'
                arr[row + 1][col + 1] = '#'
                start = '.'
            else:
                arr[row][col] = '.'
                arr[row][col + 1] = '.'
                arr[row + 1][col] = '.'
                arr[row + 1][col + 1] = '.'
                start = '#'
            col += 2
        if turn == '#':
            turn = '.'
        else:
            turn = '#'
        row += 2
        col = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end='')
        print()
    t -= 1
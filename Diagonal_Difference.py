def diagonalDifference(arr):
    diag1 = 0
    diag2 = 0
    j = 0
    for i in range(len(arr)):
        print(arr[i][j])
        diag1 += arr[i][j]
        j += 1
    j = len(arr[0]) - 1
    for i in range(len(arr)):
        print()
        diag2 += arr[i][j]
        j -= 1
    return abs(diag1 - diag2)
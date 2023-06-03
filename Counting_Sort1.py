def countingSort(arr):
    result = []
    for i in range(100):
        result.append(0)
    for i in arr:
        result[i] += 1

    return result
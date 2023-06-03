def miniMaxSum(arr):
    arr.sort()
    temp = []
    for i in arr:
        temp.append(i)
    arr.pop(-1)
    temp.pop(0)
    print(f"{sum(arr)} {sum(temp)}")
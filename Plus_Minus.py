def plusMinus(arr):
    tempuj = 0
    tempdod = 0
    tempnull = 0
    for i in arr:
        if i < 0:
            tempuj += 1
        if i > 0:
            tempdod += 1
        if i == 0:
            tempnull += 1
    print(tempdod/len(arr))
    print(tempuj/len(arr))
    print(tempnull/len(arr))
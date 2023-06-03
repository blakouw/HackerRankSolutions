def migratoryBirds(arr):
    birds = list(set(arr))
    birds.sort()
    occur = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(birds)):
            if arr[i] == birds[j]:
                occur[arr[i]] += 1
    print(occur)
    return occur.index(max(occur))
    print(birds)
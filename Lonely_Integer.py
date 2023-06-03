def lonelyinteger(a):
    for i in range(len(a)):
        unique = a[i]
        occur = 0
        for j in range(len(a)):
            print(j)
            if unique == a[j]:
                occur += 1
        if occur == 1:
            return unique
def sockMerchant(n, ar):
    socks = list(set(ar))
    number = [0] * len(socks)
    pairs = 0
    for i in range(len(ar)):
        for j in range(len(socks)):
            if socks[j] == ar[i]:
                number[j] += 1
                if number[j] % 2 == 0:
                    pairs += 1

    print(socks)
    return pairs
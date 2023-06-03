def divisibleSumPairs(n, k, ar):
    num_of_pairs = 0
    first_pair = 0
    for i in range(n):
        first_pair = ar[i]
        for j in range(n):
            #print(f"{first_pair} {ar[j]}")
            if i < j and (first_pair + ar[j])%k == 0:
                num_of_pairs +=1
    return num_of_pairs
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    lenghts = [-1,-1,-1]
    for i in range(len(sticks) - 2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            lenghts[0] = sticks[i]
            lenghts[1] = sticks[i+1]
            lenghts[2] = sticks[i+2]
            print (f"elo {sticks}")
    if sum(lenghts) == -3:
        lenghts.remove(lenghts[0])
        lenghts.remove(lenghts[1])
        return lenghts
    else:
        return lenghts
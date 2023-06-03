def breakingRecords(scores):
    maximum = 0
    minimum = 10000000000
    timesmax = 0
    timesmin = 0
    for i in scores:
        if maximum < i:
            maximum = i
            if scores.index(maximum)!=0:
                timesmax +=1
        if minimum > i:
            minimum = i
            if scores.index(minimum)!=0:
                timesmin +=1
    to_return = [timesmax,timesmin]
    return to_return
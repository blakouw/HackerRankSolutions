def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(steps):
        print(path[i])
        if path[i] == "U":
            level += 1
            if level == 0:
                valleys +=1
        elif path[i] == "D":
            level -= 1
    return valleys
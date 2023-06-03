def matchingStrings(strings, queries):
    instances_occur = []
    for i in range(len(queries)):
        instances_occur.append(0)
    for i in range(len(queries)):
        obj = queries[i]
        for j in range(len(strings)):
            if obj == strings[j]:
                instances_occur[i] += 1
    return instances_occur
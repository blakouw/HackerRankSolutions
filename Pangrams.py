import string
def pangrams(s):
    a = s.lower()
    print(a)
    alfabet = list(string.ascii_lowercase)
    alfabet.append(' ')
    missing = 0
    letters_occur = [0] * len(alfabet)
    for i in range(len(alfabet)):
        for j in range(len(a)):
            if alfabet[i] == a[j]:
                letters_occur[i] += 1
    print(alfabet)
    print(letters_occur)
    for i in range(len(letters_occur)):
        if letters_occur[i] == 0:
            missing += 1
    if missing > 0:
        return "not pangram"
    else:
        return "pangram"
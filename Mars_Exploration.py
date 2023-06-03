def marsExploration(s):
    message = 'SOS'
    letters_changed = 0
    partmess = ''
    for i in range(0,len(s)-1,3):
        partmess = s[i] + s[i+1] + s[i+2]
        for j in range(3):
            if partmess[j] != message[j]:
                letters_changed += 1
        #print(f"{s[i]}{s[i+1]}{s[i+2]} letterschanged {letters_changed}")
    return letters_changed
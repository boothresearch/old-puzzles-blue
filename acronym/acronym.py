def abbreviate(words):
    acro=[]
    data = words.split(" ")
    for w in data:
        acro.append(w[0])
        print(''.join(acro))
    return ''.join(acro)
print(abbreviate("HI Everybody From Azam"))
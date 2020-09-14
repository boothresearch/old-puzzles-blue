def rotate(text, key):
    out = ""

    for l in text:
        if l.isalpha():
            new_l = ""
            if l.isupper():
                if ord(l) + key <= ord('Z'):
                    new_l += chr(ord(l) + key)
                    print("1")
                elif ord(l) + key >= ord('Z'):
                    new_l += chr(ord(l) - key)
                    print("2")
            elif l.islower():
                if ord(l) + key <= ord('z'):
                    new_l += chr(ord(l) + key)
                    print("3")
                elif ord(l) + key >= ord('z'):
                    new_l += chr(ord(l) - key)
                    print("4")

            out += new_l 

        else:
            out += l
    
    print(out)


rotate("Zet's 12 Abc", 21)

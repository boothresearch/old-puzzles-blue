def rotate(text, key):
    out = ""

    for l in text:
        if l.isalpha():
            new_l = ""
            if l.isupper():
                if ord(l) + key <= ord('Z'):
                    new_l += chr(ord(l) + key)
                    print("1")
                elif ord(l) + key > ord('Z'):
                    new_l += chr(ord(l) + key - 26)
                    print("2")
            elif l.islower():
                if ord(l) + key <= ord('z'):
                    new_l += chr(ord(l) + key)
                    print("3")
                elif ord(l) + key > ord('z'):
                    new_l += chr(ord(l) + key - 26)
                    print("4")

            out += new_l 

        else:
            out += l
    
    return out

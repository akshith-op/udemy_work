def alphabet_position(text):
    pivot = 'a'
    alphabet = ['a']
    for i in range(25):
        pivot = chr(ord(pivot)+1)
        alphabet.append(pivot)
    ans = []
    for idx in text:
        idx = idx.lower()
        if idx in alphabet:
            ans.append(alphabet.index(idx)+1)
        else:
            pass
    f = ''
    for i in ans:
        i = str(i)
        f+=i
        f+=' '
    print(f.rstrip())
alphabet_position("The sunset sets at twelve o' clock.")

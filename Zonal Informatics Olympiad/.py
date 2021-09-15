def good(N, K):
    h = 1
    l = []
    for i in range(N):
        for j in range(K + 1):
            # for y in range(K + 1):

            # a = (i, j)
            print((j), h)
            l.append((j))
            h += 1
    print(len(l))


good(3, 3)

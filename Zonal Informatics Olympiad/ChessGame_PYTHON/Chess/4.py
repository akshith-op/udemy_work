def k(K):
    # arrset = set(arr)
    # if len(arrset)
    arr = []
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            if i == j:
                pass
            else:
                u = (i, j)
                if j % i == 0:
                    arr.append(u)

                else:
                    pass
    print(arr)
    print(len(arr) + K)


K = int(input("pls enter a number: "))
k(K)

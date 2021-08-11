# def comb(K):
#     s = []


def n_loop(N, K):
    for idx in range(N):
        for i in range(K + 1):
            if N > 0:
                n_loop(N - 1, K)
                print(i)
            # for j in range(K + 1):
            # for k in range(K + 1):

            # a = [i, j, k]
            # if a[0] == 0 and a[1] == 1 and a[2] == 0:
            #     pass


#             # else:
#             print(a)
#             s.append((i, j, k))

# print(len(s))


n_loop(6, 3)

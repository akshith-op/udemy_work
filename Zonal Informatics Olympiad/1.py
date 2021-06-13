import itertools


def good(n, k):
    for comb in itertools.combinations(list(range(k + 1)), n):
        print(list(comb))


good(4, 4)

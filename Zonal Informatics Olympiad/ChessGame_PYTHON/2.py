def function(N):
    for i in range(len(N)):
        if sum(N) <= 0 and N[i] < 0:
            N[i] *= -1
            if sum(N) > 0:
                print(N)
                print(sum(N))
                break


function([-12, -2, -16, -19, -9, -3, -7, -11, -17, -3, -15, -10, -10, -15, -8])

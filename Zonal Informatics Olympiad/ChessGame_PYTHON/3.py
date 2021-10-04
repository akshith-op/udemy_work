i = 0
def function(x, y, k):
    global i
    while x < y:
        print(x)
        x *= k
        i+=1
    while x != y:
        print(x)
        x -= 1
        i+=1
    print(x)
    print()
    print(f"{i} iterations")


function(3,10,2)


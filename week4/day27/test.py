def add(*args):
    print(sum(args))
add(3,5,6)
def correct_answer(**kwargs):
    return kwargs['a']+kwargs['b']

print(correct_answer(a = 12, b = 13))

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
recur_factorial(int(input('please enter a number: ')))
# 0 1 1 2 3 5 8 13
def fibonachi(n):
   if n==1:
       return 0
   elif n==2:
       return 1
   else:
       return fibonachi(n-1)+fibonachi(n-2)

print(fibonachi(5))

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

print(factorial_iterative(5))
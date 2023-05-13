def Fibonacci(n):
    '''The fibonacci function is a function that gives you the nth element of fibonacci series, n is the input of the function'''


    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci.__doc__)



def lucas(n):
    '''The lucas function is a function that gives you the nth element of lucas series, n is the input of the function'''

    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)
print(lucas.__doc__)

def sum_series(w , x = 0, y = 1):
    '''The sum series function is a function that takes 3 inputs and two of them are optional, the first input is the nth element
    of the series, and the other inputs is to determine the base of the series that we are creating, and these two inputs are optional 
    if you did not pass it to the function, it will act like a fibonacci series
    '''

    if x == 0 and y == 1 :
        if w == 0:
            return 0

        if w == 1 or w == 2:
            return 1
 
        
        return Fibonacci(w-1) + Fibonacci(w-2)

    if x == 2 and y == 1 :
        if w == 0:
            return 2
        if w == 1:
            return 1

        return lucas(w-1) + lucas(w-2)

        

    if w == 0  :
        return x
    if w == 1 :
        return y

    res = [x,y]
    for x in range(w):
        res.append(res[x + 1] + res[x])

    return res[w]


print(sum_series.__doc__)
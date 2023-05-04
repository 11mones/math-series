def Fibonacci(n):


    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)




def lucas(n):

    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(w , x = 0, y = 1):

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



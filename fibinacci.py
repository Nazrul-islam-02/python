
def fibo(n):
    c = 0
    a = 0
    b = 1
    print(a,b,end= " ")
    while(c<n-2):
        print(a+b, end=" ")
        t = a + b
        a = b
        b = t
        c = c+1
        

fibo(7)

n=0
def fib(n):
    global n
    n+=1
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
    global f,c
    f=[]
    c=[]
def m(n):
    for i in range(n):
        global n
        n=0
        f.insert(i,fib(i))
        c.insert(i,n)
    print(f)
    print(c)
m(10)        
    
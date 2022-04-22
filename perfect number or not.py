def perfect(n):
    a=n
    p=0
    for i in range(1,n):
        if(n%i==0):
            p+=i
        else:
            p+=0
    if(p==a):
        print('perfect number')
    else:
        print('not perfect number')
x=int(input('enter a number'))
perfect(x)
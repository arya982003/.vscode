def palindrone(n):
    a=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if(a==s):
        print(a,'is palindrone')
    else:
        print(a,'is not palindrone')
n=int(input('enter a number'))
palindrone(n)
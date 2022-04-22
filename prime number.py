def prime(n):
    i=2
    f=False
    while(i<=n/2):
        if(n%2==0):
          f=True
          break
        i+=1
    if(f==False):
        print(n,'is prime no.')
    else:
        print(n,'is not prime no.')
n=int(input('enter a number'))
prime(n)
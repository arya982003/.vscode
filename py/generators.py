def cube(l):
    for i in range(1,l+1):
        yield i**3
        
def fib(limit):
    a,b=0,1
    for i in range(limit):
        yield a
        a,b=b,a+b
        
for c in cube(10):
    print(c)
    
for f in fib(15):
    print(f,end=" ")
    
# wap to generate a list of even sqr using generators
# wap to generate a list of acronymns from a list of words using generators

def sqr(limit):
    
    
    
    
    
    
def acr(*words):
    for w in words:
        yield ' '.join([i[0].upper() for i in  w.split()()])
for words in 
print('first pattern:')
for i in range(1,6):
    print()
    for j in range(i):
        print("*",end=' ')
print('\nfirst pattern:')
for i in range(1,9):
    print()
    for j in range(1,i):
        print(j,end=' ')
print('\nthird pattern:')
for i in range(0,8):
    print()
    for j in range(i):
        print(i,end=' ')
print('\nfourth pattern:')

c=0
for i in range(1,5):
     for j in range(i):
         print(c,end=' ')
         c+=1
     print(" ")
print('fifth pattern')
n=5
for i in range(1,n+1):
    for j in range(n,i-1):
        print(" ",end=' ')
    for k in range(1,i+1):
         print(k,end=' ')
    for l in range(i-1,0,-1):
        print(l,end=' ')
        print()
        
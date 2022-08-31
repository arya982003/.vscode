import operator
from re import I
'''d={1:2,3:4,4:3,2:1,0:0}
print(d)
sd=sorted(d.items(),key=operator.itemgetter(1)) #assending order
print(sd)
sdd=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True)) # descending order
print(sdd)
print('\n')
d1={1:10,2:20}
d2={3:40,4:50}
d3={5:50,6:60}
print(d1|d2|d3)
l1=[1,2,3]
l2=['red','blue','green']
d=dict(zip(l1,l2))
print(d)
d={'name':'sachin','age':'25','name':'pragya','age':'29'}
print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))
print(d.pop('age'))
print(d)
print(d.clear())'''
d={}
n=int(input("enter the terms:"))
for i in range(1,n+1):
    d[i]=i*i
print(d)
    
a=range(1,21)
sum=0
print('the numbers which are divisible 2,3or 5')
for i in a:
    if(i%2==0 or i%3==0 or i%5==0):
        pass
    else:
        print(i)
        sum+=i
print('sum=',sum)
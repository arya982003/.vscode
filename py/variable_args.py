# how many parameter in a function

'''


that is called variable arguments
we define a function with *args as Parameter
where args is the name of Parameter
'''
def multiplier(*numbers):
      out=1
      for var in numbers:
          out*=var
      return out
  
print(multiplier(2,3,4,5))
print(multiplier(2,3,4,5,6,7,8,9))
print(multiplier())
print(multiplier(3,3))  
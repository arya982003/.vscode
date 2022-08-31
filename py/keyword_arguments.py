from ast import arguments
from sqlalchemy import func


'''
we have another way in python that will allow us to pass named arguments to a function
that is called keyword arguments
**kwargs
kwargs is the name of the parameter and ** before it means that it can accept 
any number of named values in a function
'''
def student_report(**kwargs):
    total=0
    for k,v in kwargs.items():
        print(k,v)
        total+=v
    return len(kwargs),total/len(kwargs)
print(student_report(rohan=50,rani=30,alka=55))
print(student_report(rohan=50,rani=30,alka=88,abhay=77,vijay=99))
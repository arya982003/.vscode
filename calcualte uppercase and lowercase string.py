def calcu(a,sup=0,slo=0):
    for i in a:
        if(i.isupper()):
            sup+=1
        elif(i.islower()):
            slo+=1
        else:
            pass
    print('no of uppercase character',sup)
    print('no of lowercase character',slo)
str=input('enter the string')
calcu(str)
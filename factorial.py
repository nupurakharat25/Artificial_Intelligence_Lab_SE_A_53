num=int(input("Enter any number"))
def fac(num):
    if num==1 or num==0:
       return 1
    else :
       return num*fac(num-1)
print("factorial of given number:",fac(num))


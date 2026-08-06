r=int(input("enter the total marks of subject"))
a=int(input("enter the marks of maths"))
b=int(input("enter the marks of physics"))
c=int(input("enter the marks of chemistry"))
d=int(input("enter the marks of english"))
e=int(input("enter the marks of biology"))
avg=((a+b+c+d+e)/5)
percentage=((avg/r)*100)
print("the total percentage is",((avg/r)*100))
if(percentage<=40):
	print("fail")
elif(percentage<40):
	print("II class")
elif(percentage<=65):
	print("I class")
elif(percentage<=75):
	print("Distinction")
else:
	print("outstanding")

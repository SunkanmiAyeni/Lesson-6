print("enter the marks for 5 subjects")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
sum=m1+m2+m3+m4+m5
average=sum/5
if average>91:
    print("you are in grade 1")
elif average>81:
    print ("you are in grade 2")
elif average>61:
    print ("you are in grade 3")
elif average>35:
    print("youre in grade 4")
else:
    print("you have failed")
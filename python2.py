# fibonacci series

n = int(input("enter number how many number you want in series: "))
a = 0
b = 1
s = 0

if n==0:
    print("invalid input")
elif n==1:
    print("0")
elif(n==2):
    print("0 1")
else:
    print(a,b,end =" ")
    for i in range(3,n+1):
        s = a+b
        print(s,end = " ")
        a = b
        b = s

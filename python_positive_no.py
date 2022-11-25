# print all positive number in range


list1=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    list1.append(e)

print("Positive numbers in",list1,"are: ")
  

for i in list1:   
    if i >= 0:
       print(i, end = " ")




    



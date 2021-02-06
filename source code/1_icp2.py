#1. Write a program, which reads height (feet.) of N students into a list and convert these heights to cm in a separate list:
L1=[]### list array
n=int(input("Enter number of students :"))### asking for input from user
for i in range(0,n):
    ele = input()
    L1.append(ele)### appending inputs from user
print(L1)##printng list
abc=float(L1[0])
de=float(L1[1])
ghi=float(L1[2])
jkl=float(L1[3])
cm=[abc/0.0328,de/0.0328,ghi/0.0328,jkl/0.0328]##validating user input to output
print("length in cm:",round(cm[0],1),round(cm[1],1),round(cm[2],1),round(cm[3],1))### printing output

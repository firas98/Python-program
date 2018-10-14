#this is the program to implement the simple calculator
#input the number a and b
a=input("Please enter the number a\n")
b=input("Please enter the number b\n")
a=float(a)
b=float(b)
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
option=input("Selct your choice\n")
if option == '1':
    c=a+b
    print(c)
elif option =='2':
    c=a-b
    print(c)
elif option == '3':
    c=a*b
    print(c)
elif option == '4':
    c=a/b
    print(c)
else:
    print("Inalid Option")

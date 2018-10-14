print("Welcome to the Assil Canteen")
print("1.Veg")
print("2.Non-Veg")
items=[]
count=0
price=0
option=input("Select one of the following options given above")
#if the user selects the veg option
if option == '1':
    print("1.Masala Dosa")
    print("2.Idli")
    print("3.Veg Puff")
    print("4.Fried Rice")
    print("5.Paneer Frankie")
    option1=input("Select your option given above")
    if option1 == '1':
        items.append("Masala Dosa")
        count=count+1
        price=price+30
    elif option1 == '2':
        items.append("Idli")
        count=count+1
        price=price+20
    elif option1 == '3':
        items.append("Veg Puff")
        count=count+1
        price=price+12
    elif option1 == '4':
        items.append("Freid Rice")
        count=count+1
        price=price+20
    elif option1 == '5':
        items.append("Paneer Frankie")
        count=count+1
        price=price+34
    else:
        print("Please enter the valid option")
    
elif option =='2':
    print("Chicken Biryani")
    print("Chicken Puff")
    print("Chicken Fried Rice")
    option2=input("Please select from one of the Following items")
    if option2 == '1':
        items.append("Chicken Biryani")
        count=count+1
        price=price+50
    elif option2 == '2':
        items.append("Chicken Puff")
        count=count+1
        price=price+20
    elif option2 == '3':
        items.append("Chicken Fried Rice")
        count=count+1;
        price=price+30
    else:
        print("Please select from one of the following options")

else:
    print("Please select one of the following options given below")


print("Your Bill is as follows")
print(items)
print(price)
print(count)


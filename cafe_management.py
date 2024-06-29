# we have used dictionary to  make the menu bcz it is a database hich gives us a functionality to add both the name and the price of the menu 

menu={
    "pizza":400,
    "burger":80,
    "coffee":50,
    "chicken":360,
    "panner":300,
    "naan":40
}


print("-----------------**WELCOME TO OUR PYTHON CAFE :)**-----------------")
print("-----------------------------**MENU**-----------------------------")
print("Pizza Rs400\nBurger Rs80\nCoffee Rs50\nChicken Rs360\nPaneer Rs300\nNaan RS40")

order_price=0

try:
    item_1=input("Enter your First item you want to order: ")
    if item_1 in menu:
        order_price += menu[item_1]
    print(f"your order of {item_1} is been confirmed ")
except:
    print(f"your dezired itme is not avaiable at the moment")
    
try:
    Next=input("Do you want to order another item? (Yes/No) ").lower()
    if Next == "yes":
        item_2=input("Enter your second item you want to order: ")
        item_2.lowercase()
        if item_2 in menu:
            order_price += menu[item_2]
            print(f"your order of {item_2} is been confirmed ")            
except:
    print(f"your dezired itme is not avaiable at the moment")   
finally:
    print(f"your bill for the order is  Rs{order_price}")
    print("please pay the bill:)")
    print("thanyou:) visit again!")


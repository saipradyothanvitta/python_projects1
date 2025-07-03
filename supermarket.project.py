name=input("Name:")

lists='''
potato       Rs 10/kg
Sugar      Rs 8/kg
onion        Rs 30/liter
carrot       Rs 25/kg
Paneer     Rs 40/kg
tofu     Rs 12/pack
butter      Rs 200/pack
'''

price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

items = {'potato':10, 'sugar':8, 'onion':30, 'carrot':25, 'paneer':40, 'tofu':12, 'butter':200}

while True:
    option=input("Select 1 for list & 2 for exit: ")
    if option=='2':
        print("**...Thanks For Shopping...**")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1=input("Select 1 For Buy & 2 for exit: ")
            if inp1=='2':
                print("**...Thanks For Shopping...**")
                break
            elif inp1=='1':
                item=input("Choose Your Items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  # Check if input is a digit
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            discount = (totalprice*5)/100
            finalamount = tax + totalprice - discount

            print(25 * "=", "A's Supermarket", 25 * "=")
            print(28 * " ", "Greater Noida,U.P")
            print("Name:", name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print("Discount", 50* " ", 'Rs', discount)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "**----.1...Thank you & Visit again....----**")
            print(75 * "-")
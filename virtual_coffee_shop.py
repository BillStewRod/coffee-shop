#This is Mandingo's Coffe Shop
#Greet your customer
print("Hello, welcome to Mandingo's Coffee!!!!!!!!!!!!!!")

#Ask your customer 
name = input("What is your name?\n")
#or name == "YES" or name == "yES" 
#Greet the customer with their name and thank them for coming in today using concatenation.
if name == "Alison" or name == "alison" or name =="ALISON" or name =="aLISON":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4 :
        print("You're not welcome here Alison!! Get the fuck out!!")
        exit()
    else:
        evil_status = input("Are you sure?\n")
        if evil_status == "no" or name == "NO" or name == "nO":
            print("You're not welcome here Alison!! Get the fuck out!!")
            exit()
        else:
            print("Oh, so you must be one of the good not evil Alison, I guess you can come in. But wait...\n")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")

#Ask if the person has a beard
beard = input("Do you have a beard?\n")

if beard == "no" or name == "NO" or name == "nO":
  print("Get the fuck out, and come back when you grow one!!")
  exit()
else:
  beard =input("Nice beard, How Long is it?\n")

#How long is the beard
if beard >= "2":
  print("Myyyy Nigga! You can go in to the front of the line\n")
else:
  print("Get the fuck out, and come back when you have a beard longer than 2 inch!!")
  exit()
  
#Coffee menu
menu = " Black Coffee\n Americano\n Espresso\n Latte\n Cappucino\n Frappuccino\n Flat White\n Cafecito\n"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

prices = {
"Black Coffee": 5,
"Americano": 6,
"Espresso": 8,
"Latte": 9,
"Cappucino": 10,
"Frappuccino": 13,
"Flat White": 9,
"Cafecito": 10
}

while order not in prices:
    print("Sorry, that item is not on the menu. Please choose from the following:")
    order = input(menu + "\n")
#Calculate the customer's total
total = prices[order] * int(quantity)

#Give the customer their total
print("Sounds good " + name + "! Thank You for your order. Your total is: $" + str(total))

#Final statement
print("We'll have your " + quantity + " " + order + " ready for you in a moment.")
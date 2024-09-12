# Write a program that displays the following information for a student:
# Name 
# Address, with city, state, and ZIP
#Telephone number   
#College major 

name='Cameron Calero'
address='2045 Heliport Loop'
City='Riverfolk,'
State='IN'
Zip='43286'
Tele='812-555-1212'
print(name + '\n' + address + '\n' + City + ' ' + State + ' ' + Zip + '\n' + Tele)

#Write a program that ask the user to enter the projected ammount of total sales,then displays the profit.
#Get the projected total sales.
total_sales=float(input('Enter the projected sales: '))
#Calculate the profit as 23 percent of total sales.
profit=total_sales * 0.23
#Display the profit.
print('The profit is $',format(profit, ',.2f'))

#Write a program that ask the user to enter the total square feet in a tract of land and calculates the number of acres in the tract.
total_sqft=int(input('Enter SQ FT: '))
acres=total_sqft / 43_560
print('The Acres are:',format(acres, ' ,.2f'))

#Write a program that ask for the price of each item, then displays the subtotal of the sale, the ammoun of sales tax, and the total.
sales_tax_rate=0.07
subtotal=0
for i in range(1,6):
    price=float(input(f'Enter the price of item {i}: '))
    subtotal+= price 

sales_tax=subtotal * sales_tax_rate
total=subtotal + sales_tax

print(f'\nSubtotal: ${subtotal:,.2f}')
print(f'Sales Tax: ${sales_tax:,.2f}')
print(f'Total: ${total:,.2f}')

#Write a program that displays the distance at certain time periods while the car is going 70 miles per hour
Speed=70 

time_6_hours=6
time_10_hours=10
time_15_hours=15
distance_6_hours=Speed * time_6_hours
distance_10_hours=Speed * time_10_hours
distance_15_hours=Speed * time_15_hours

print(f'The distance the car will travel in 6 hours is: {distance_6_hours} miles')
print(f'The distance the car will travel in 10 hours is: {distance_10_hours} miles')
print(f'The distance the car will travel in 15 hours is: {distance_15_hours} miles')

#Write a program that will ask the user to enter the amount of a prucharse. 
#The program should then compute the state and county sale tax.
#The program should display the amount of the purchase, the state sales tax, the county sales tax.
state_tax_rate=0.05
county_tax_rate=0.025

Purchase_amount=float(input("Enter the amount of the purchase: "))
state_tax= Purchase_amount * state_tax_rate
county_tax= Purchase_amount * county_tax_rate
total_sales_tax= state_tax + county_tax
total_cost= Purchase_amount + county_tax

print(f'Amount of purchase: ${Purchase_amount:.2f}')
print(f'State sales tax: ${state_tax:.2f}')
print(f'County sales tax: ${county_tax:.2f}')
print(f'Total sales tax: ${total_sales_tax:.2f}')
print(f'Total ammount(including taxes): ${total_cost:.2f}')        

#Write a program that ask the user for the number of miles driven and the gallons of gas used.
miles_driven=float(input('Enter the number of miles driven: '))
gallons_used=float(input('Enter the number of gallons of gas used: '))
Mpg=miles_driven / gallons_used
print(f"The car's MPG is: {Mpg: .2f}")

#Write a program that calculates the total amount of a meal purchased at a restaurant
#The program should ask the user to enter the charge for the food, then calculate the ammounts 18 percent tip and 7 percent sales tax.
SALES_TAX_RATE = 0.07
TIP_RATE = 0.18

food_charge = float(input("Enter the charge for the food: $"))

sales_tax = food_charge * SALES_TAX_RATE
tip = food_charge * TIP_RATE
total_amount = food_charge + sales_tax + tip

print(f"\nCharge for the food: ${food_charge:,.2f}")
print(f"Sales Tax (7%): ${sales_tax:,.2f}")
print(f"Tip (18%): ${tip:,.2f}")
print(f"Total Amount: ${total_amount:,.2f}")

#write a program that converts celsius temperatures to Fahrenheit temperatures.
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

# write a program that asks the user how many cookies he or she wants to make, then d displays the number of cups of each ingredient needed for the specified number of cookies. 
sugar = 1.5
butter = 1
flour = 2.75
cookies_in_recipe = 48

desired_cookies = int(input("Enter the number of cookies you want to make: "))
total_cookies = desired_cookies / cookies_in_recipe

sugar_needed = sugar * total_cookies
butter_needed = butter * total_cookies
flour_needed = flour * total_cookies

print(f"\nTo make {desired_cookies} cookies, you need:")
print(f"{sugar_needed:.2f} cups of sugar")
print(f"{butter_needed:.2f} cups of butter")
print(f"{flour_needed:.2f} cups of flour")

#Write a program that ask the user for the number of lions and the number of tigers in the zoo.
amount_tigers=int(input("Enter the number of Tigers at the zoo:"))
amount_lions=int(input("Enter the number of Lions at the zoo: "))

total_cats = amount_tigers + amount_lions
percent_tigers=(amount_tigers / total_cats)* 100
percent_lions= (amount_lions / total_cats)* 100

print(f"\nPercentage of Big Cats at the Zoo: ")
print(f"{percent_tigers:.0f}% Tigers")
print(f"{percent_lions:.0f}%  Lions")

#Write a program that displays the following information: 
#ammount joe paid for the stock 
#ammount of commission Joe paid his broker when he bought the stock
# amount for which joe sold the stock
#ammount of commission Joe had to pay his broker when he sold the stock
#Ammount of money Joe had left when he sold the stock and paid hsi broker(twice). If this amount is postive, then joe made profit, If the amount is negative, then Joe lost money.
number_of_shares= 2000
purchase_price_per_share= 40.00 
commission_rate= 0.03

total_purchase_amount= number_of_shares * purchase_price_per_share
commission_cost=total_purchase_amount * commission_rate
total_amount_spent=total_purchase_amount + commission_cost

selling_price_per_share=purchase_price_per_share
total_selling_amount= number_of_shares * selling_price_per_share
sell_comission=total_selling_amount * commission_rate
total_amount_received= total_selling_amount - sell_comission
profit_or_loss= total_amount_received - total_amount_spent
print(f'Amount of money Joe Paid: ${total_purchase_amount:.2f}')
print(f'Amount of commision Joe paid his broker when he bough it: $ {commission_cost:.2f}')
print(f'Amount of which Joe sold the stock: $ {total_selling_amount:.2f} ')
print(f'Amount of comission Joe paid his broker when he sold the stock: $ {sell_comission:.2f}')
print(f'Amount Joe had left after selling then stock and paying his broker: $ {total_amount_received:.2f}')
if profit_or_loss > 0:
    print(f'Joe made a profit of ${profit_or_loss:.2f}')
else:
    print(f'Jose lost ${abs(profit_or_loss):.2f}')

#Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following
#The length of the row, in fee
#The amount of space used by an end-post assembly,in feet.
#The amount of space between the vines, in feet.
R=float(input('Enter the length of the row (in ft): '))
E=float(input('Enter the ammount of space in Ft used by an end-post assembly: '))
S=float(input('Enter the space between vines(in ft): '))
v=(R-2*E) /S
 
print(f'The number of grapevines that will fit in the row: {int(v)}')

##Write a program that makes the calculation for you. The program should ask the user to input the following:
#The amount of principal originally deposited into the account
#The annual intrest rate paid by the account
#The number of time per year that intres is compounded 
#the number of years the account will be left to earn intrest 
P=float(input('Enter the Principal amount deposited: '))
R=float(input('Enter the annual interest rate: '))
N=int(input('Enter the number of times the intrest is compounded per year: '))
T= float(input('Enter the number of years the account will be left to earn intrest: '))
A= P * (1 + R/N)**(N*T)

print(f'The amount of money in the account after {T:.0f} years: $ {A:.2f}')

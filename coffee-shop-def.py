"""
• Author: Boyeong Yoon (boyeong.nancy.yoon@gmail.com)
• Date: May 13, 2022

• 3 functions
  - order()	
    : returns size, coffee, flavor
  - calculate(size, coffee, flavor)
  	: returns total_price, tip, total_price_tip
  - display(total_price, total_price_tip)
  	: prints out what the user ordered and the total price with 15% tip
"""





""" 
Asks the user what size, coffee, and flavor they want
@return		size, coffee, flavor
"""
def order():
	# Asks the user what size cup they want, choosing between small, medium, and large
	while True:
		size = input("\t (1) Size? ").lower()

		if size in ['small', 'medium', 'large']:
			break


	# Asks the user what kind of coffee they want, choosing between brewed, espresso, and cold brew
	while True:
		coffee = input("\t (2) Coffee? ").lower()

		if coffee in ['brewed', 'espresso', 'cold brew']:
			break


	# Asks the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel
	while True:
		flavor = input("\t (3) Flavor? (if you don't want, please enter 'None') ").lower()

		if flavor in ['hazelnut', 'vanilla', 'caramel', 'none']:
			break

	return size, coffee, flavor



"""
Calculates the coffee price and rounds the cost with tip to two decimal places
@input 		size, coffee, flavor
@return 	total_price, tip, total_price_tip
"""
def calculate(size, coffee, flavor):
	# Menu Price in Dictionary
	size_price = {
		'small': 2,
		'medium': 3,
		'large': 4
	}

	coffee_price = {
		'brewed': 0,
		'espresso': 0.5,
		'cold brew': 1
	}

	flavor_price = {
		'hazelnut': 0.5,
		'vanilla': 0.5,
		'caramel': 0.5,
		'none': 0

	}

	# Calculates the price of the coffee
	total_price = size_price[size] + coffee_price[coffee] + flavor_price[flavor]

	# Rounds the cost with tip to two decimal places
	# e.g. medium-sized espresso with hazelnut flavor - $4, with a tip $4.60
	tip = total_price * 0.15
	total_price_tip = round(total_price + tip, 2)

	return total_price, tip, total_price_tip



"""
Displays a summarization what the user ordered and the total cos with a 15% tip
@input	 	total_price, total_price_tip
@print out 	what the user ordered and the total price with 15% tip
"""
def display(total_price, total_price_tip):
	# Display a statement that summarizes what the user ordered
	print("\t You ordered {}-sized {} with {} flavor ☕.\n".format(size, coffee, flavor))

	# Display the total cost of the cup of coffee as well as the cost with a 15% tip
	print("\t So, the total is ${}, and the total with a 15% tip is ${}.\n\n".format(total_price, total_price_tip))









print("====================================================================")
print("====================== ☕ Welcome to ⭐bucks ☕ ====================")
print("==================================================================== \n\n")

print("\t SIZE \t\t COFFEE \t\t FLAVOR (+$0.5)")
print("\t - Small   $2 \t - Brewed          \t - Hazelnut")
print("\t - Medium  $3 \t - Espresso (+$0.5)\t - Vanilla")
print("\t - Large   $4 \t - Cold Brew (+$1) \t - Caramel \n\n")



print("\t What would you like to order today? \n")

size, coffee, flavor = order()
print("\n\n")
total_price, tip, total_price_tip = calculate(size, coffee, flavor)
display(total_price, total_price_tip)



print("====================================================================")
print("======================= ☕ Have a good day ☕ ======================")
print("====================================================================")

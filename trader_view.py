class View:

	def type_user(self):
		type_ = input("Hi, there! Welcome to the stock trader app. Are you a new user or existing user? Type 'n' or 'e'!\n")
		return type_.lower()

	def username(self, error):
		username = input("What is your username?\n")
		return username
	
	def password(self):
		pass_ = input("What is your password?\n")
		return pass_


	def main_menu_admin(self, error = None):
		print("\033c")

		if error:
			print(error)


		print('='*30)
		print("  ")
		print("  ")
		print(" ")
		print(" ")
		print("OPTIONS:	VIEW LEADERBOARD		QUIT")
		print("           ('L')            		('X')")
		print("  ")
		print("  ")
		return input('\n').lower()strip()


	def main_menu_user(self, error=None):
		print("\033c")

		if error:
			print(error)


		print('='*30)
		print("  ")
		print("  ")
		print(" ")
		print(" ")
		print("OPTIONS:	BUY STOCK		SELL STOCK		VIEW DASHBOARD		QUIT")
		print("           ('B')            ('S')           ('D')            ('X') ")
		print("  ")
		print("  ")

		return input('? \n').lower()strip()

	
	def ticker(self, error=None):
		print("\033c")
		if error:
			print(error)
		ticker = input("Please enter the ticker of the company whose stock you wish to buy/sell:\n")
		return ticker

	def last_price(self, last_price, ticker):
		print("The price of" + str(ticker) + "is" + str(last_price) + "per share.")
		return input("Would you still like to buy/sell the stock[y/n]?")

	def num_shares(self, ticker):
		return input("How many shares of " + str(ticker) + "would you like to buy/sell? \n")

	def buy(self, error=None):
		if error:
			print("You do not have enough money to complete this transaction. You will now return to the main menu.")


	def view_dashboard(self, dashboard):
		# print("Welcome to your dashboard, " + str(self.username) + "!\n")
		# print("Your current account balance is: " )
		print("Your current account:")
		print(dashboard)

	def view_leaderboard(self, leaderboard):
		print("The leaderboard:")
		print(leaderboard)


	def exit(self):
		print("\033c")
		return input('Are you sure[y/n]?').strip()

	# """
	# 101|maria92|363KJZ1q_#|admin
	# 100|sean23|iS_9IhFcwz|client
	# """
		



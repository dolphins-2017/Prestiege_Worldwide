class View:
	#print/input
	def __init__(self):
		pass


	def type_user(self):
		type_ = input("Hi, there! Welcome to the stock trader app. Are you a new user or existing user? Type 'n' or 'e'!\n")
		return type_.lower()

	def new_user(self):
		new_acct_username = input("Welcome to your new trading paradice. What would you like your username to be?\n")
		new_acct_pass = input("And your password?\n")
		return new_acct_username, new_acct_pass

	def username(self):
		username = input("What is your username?\n")
		return username
	
	def password(self):
		pass_ = input("What is your password?\n")
		return pass_

	def main_menu_user(self):
		print("Welcome to your dashboard, " + str(self.username) + "!\n")
		print("Your current account balance is: " )

	def main_menu_admin(self):
		#view leaderboard, quit
		pass


	# """
	# 101|maria92|363KJZ1q_#|admin
	# 100|sean23|iS_9IhFcwz|client
	# """
		



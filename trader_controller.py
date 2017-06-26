import trader_models
import trader_view
import get_lastprice

class Controller:
	def __init__(self):
		self.view = trader_view.View()
		self.type_ = None
		self.username = None
		self.password = None

	def type_user(self):
		type_ = self.view.type_user()
		self.type = type_
		if type_ == "n":
			self.new_user()
		elif type_ == "e":
			self.username = self.view.username()
			self.password = self.view.password()


	def new_user(self):
		self.username = self.view.username()
		self.password = self.view.password()
		userinstance = trader_models.User(self.username, self.password)
		userinstance.create_user()


	def is_valid(self):
		userinstance = trader_models.User(self.username, self.password)
		user_is_valid = userinstance.username_is_valid()
		pass_is_valid = userinstance.password_is_valid()
		if user_is_valid and pass_is_valid == True:
			print(" ")
			print(" ")
			print('Loading dashboard....')
			return True
		else:
			return False

		#100|sean23|iS_9IhFcwz|client


	def main_menu(self):
		userinstance = trader_models.User(self.username, self.password)

		print('='*30)
		print("  ")
		print("  ")
		print(userinstance.view_dashboard())
		print(" ")
		print(" ")
		print("OPTIONS:	(BUY STOCK)		(SELL STOCK)		(QUIT)")
		print("  ")
		print("  ")



	def parse_input():
		#EX:	if pick == 'e':
			#self.encrypt()
		#if pick == 'd':
			#self.decrypt()
		#if pick == 'x':
			#self.exit()
			pass
	def buy():
		pass
	def sell():

		pass
	def view_dashboard():
		pass
	def view_leaderboard():
		pass


def main():
	test = Controller()
	user_type = test.type_user()
	validity = test.is_valid()
	if validity == True:
		test.main_menu()


main()
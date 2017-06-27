from trader_models import Terminal_Trader_App
import trader_view
import get_lastprice

class Controller:
	def __init__(self):
		self.view = trader_view.View()
		self.type_ = None
		self.username = None
		self.password = None
		self.trader_app = None

	def type_user(self):
		type_ = self.view.type_user()
		self.type = type_
		if type_ == "n":
			#create new user
			self.new_user()
		elif type_ == "e":
			#have the user login (enter username and password) until the username and password match
			is_valid = False
			while not is_valid:
				self.username = self.view.username()
				self.password = self.view.password()
				self.trader_app = Terminal_Trader_App(self.username, self.password)
				is_valid = trader_app.user.password_is_valid()




	def new_user(self):
		#have user input username and check if username already exists
		is_valid = False
		while not is_valid:
			self.username = self.view.username()
			trader_app_init = Terminal_Trader_App(self.username)
			is_valid = trader_app_init.user.username_is_valid()

		#have the user input their password
		self.password = self.view.password()

		#log the user in by creating an instance of the Terminal Trader App
		self.trader_app = Terminal_Trader_App(self.username, self.password)
		#create a record of the user and create an account for the user
		self.trader_app.user.create_user()

	def permission_level(self):
		#find permission_level
		permission_level = self.trader_app.user.find_permission_level()
		print(permission_level)
		main_menu(permission_level)


	def main_menu(self, permission_level, error=None):
		#takes permission level, displays correct menu
		if permission_level == 'client':
			pick = self.view.main_menu_user()
			if pick in ['b', 's', 'd', 'x']:
				self.parse_menu(pick)
			else:
				pick = self.view.main_menu_user('invalid option!\n=============')
				self.parse_menu(pick)

		if permission_level == 'admin':
			pick = self.view.main_menu_admin()
			if pick in ['l', 'x']:
				self.parse_menu(pick)
			else:
				pick = self.view.main_menu_admin('invalid option!\n=============')
				self.parse_menu(pick)

	def parse_menu(self, pick):
		if pick == 'l':
			self.view_leaderboard()
		if pick == 'b':
			self.buy()
		if pick == 's':
			self.sell()
		if pick == 'd':
			self.view_dashboard()
		if pick == 'x':
			self.quit()

	def get_last_price(self, ticker):
		last_price = self.trader_app.game.get_info(ticker)
		chocie = self.view.last_price(last_price, ticker)
		return choice

	def buy(self):
		ticker = self.view.ticker()
		choice = self.get_last_price(ticker)
		if pick == 'y':
			num_shares = self.view.num_shares(ticker)
			status = self.trader_app.game.buy(ticker,num_shares)
			if status == False:
				self.view.buy(error)
			self.permission_level()
		else:
			self.permission_level()

	def sell(self):
		ticker = self.view.ticker()
		choice = self.get_last_price(ticker)
		if pick == 'y':
			num_shares = self.view.num_shares(ticker)
			self.trader_app.game.sell(ticker,num_shares)
			self.permission_level()

		else:
			self.permission_level()

	def view_dashboard(self):
		dashboard = self.trader_app.user.view_dashboard()
		return self.view.view_dashboard(dashboard)

	def view_leaderboard(self):
		leaderboard = self.trader_app.admin.view_leaderboard()
		return self.view.view_leaderboard(leaderboard)

	def quit(self):
		pick = self.view.exit()
		if pick == 'y':
			exit(0)
		else:
			self.permission_level()




def main():
	test = Controller()
	test.type_user()
	test.permission_level()
	#validity = test.is_valid()
	#if validity == True:
		#test.main_menu()

#if name == main():
main()
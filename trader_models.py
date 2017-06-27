import requests
from dbmanager import UserDBManager, TransactionsDBManager
from get_lastprice import Markit

class Terminal_Trader_App:

	# communicate with controller
	def __init__(self, username, password = None, num_shares = None, ticker = None):
		self.username = username

		if password == None:
			self.user = User(self.username)
		else:
			self.password = password
			self.user = User(self.username, self.password)
			self.admin = Admin(self.username, self.password)

		if num_shares == None:
			num_shares = 0
			self.num_shares = num_shares
		else:
			self.num_shares = num_shares

		if ticker == None:
			ticker = ""
			self.ticker = ticker
		else:
			self.ticker = ticker



		self.markit = Markit()
		self.game = Game(self.username)



class Game:
	def __init__(self, username = None):
		self.markit = Markit()
		self.username = username
		self.db_manager = TransactionsDBManager()

	def get_info(self, ticker):

		info = self.markit.get_quote(ticker)
		if "LastPrice" in info:
			return(info["LastPrice"])


	def buy(self, ticker, num_shares):

		last_price = self.get_info(ticker)
		
		return self.db_manager.buy(self.username, num_shares, ticker, last_price)

	def sell(self, ticker, num_shares):
		last_price = self.get_info(ticker)
		return self.db_manager.sell(self.username, num_shares, ticker, last_price)

class User: 
		#get username, password, get corresponding data 
	def __init__(self, username, password=None):
		self.username = username
		if password == None:
			self.password = ""
		else:
			self.password = password
		self.db_manager = UserDBManager()


	def find_permission_level(self):
		permission_level = self.db_manager.find_permission_level(self.username)
		return permission_level

	def username_is_valid(self):
		#check if username already exists

		is_valid = self.db_manager.check_username(self.username)
		return is_valid

	def password_is_valid(self):
		#check if username and password match
		is_valid = self.db_manager.check_password(self.username, self.password)
		return is_valid

	def create_user(self):
		self.db_manager.create_client(self.username, self.password)
		self.db_manager.create_account(self.username)

	def view_dashboard(self):
		dashboard = self.db_manager.view_dashboard(self.username)


		return dashboard

class Admin: #Jimmy
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.db_manager = UserDBManager()

	def find_permission_level(self):
		permission_level = self.db_manager.find_permission_level(self.username)
		return permission_level

	def username_is_valid(self):
		#check if username and password match
		is_valid = self.db_manager.check_username(self.username)
		return is_valid

	def password_is_valid(self):
		is_valid = self.db_manager.check_password(self.username, self.password)
		return is_valid

	def create_admin(self):
		return self.db_manager.create_admin(self.username, self.password)


	def view_leaderboard(self):
		return self.db_manager.view_leaderboard()





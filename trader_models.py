import requests
from dbmanager import UserDBManager, TransactionsDBManager
from get_lastprice import Markit

class Terminal_Trader_App:

	# communicate controller
	def __init__(self, username = None, password = None, amount = None, ticker = None):
		self.username = username
		self.password = password
		self.num_shares = num_shares
		self.ticker = ticker


		self.user = User(self.username, self.password)
		self.admin = Admin(self.username, self.password)
		self.markit = Markit()
		self.Game = Game(self.username, self.ticker, self.num_shares)



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
	def __init__(self, username = None, password = None):
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

	def create_user(self):
		return self.db_manager.create_client(self.username, self.password)

	def view_dashboard(self):
		dashboard = self.db_manager.view_dashboard(self.username)


		return dashboard

class Admin: #Jimmy
	def init(self, username = None, password = None):
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





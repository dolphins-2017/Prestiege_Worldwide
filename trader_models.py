import requests
class Terminal_Trader_App:

	# communicate controller
	def __init__(self):
		self.username = username
		self.password = password
		self.created_on = created_on
		self.user_id = user_id
		self.permission_level = permission_level
		self.balance = balance
		self.account_number = account_number
		self.id = id_
		self.user_id = user_id
		self.amount = amount


		self.markit = Markit()
		self.account = Account(self.balance, self.account_number, self.id, self.user_id, self.amount)

class Markit:

    def __init__(self):
        # ?input=
        self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
        # ?symbol=
        self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"
    def company_search(self,company_name):
        self.company_name = str(company_name)
        request = requests.get("http://dev.markitondemand.com/Api/v2/Lookup/json?input=" + company_name)
        info = request.json()
        print(info)
        return(info)
    def get_quote(self,ticker):
        self.ticker = str(ticker)
        request = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + ticker)
        info = request.json()
        
        if "LastPrice" in info:
            print(info["LastPrice"])


class Game:

	def get_info(self, company_name):
		#use API stuff
		#to search companies and get the exact stock ticker symbol we want. 
		#Our users also want to retreive the market data for a stock before they purchase it - we should obviously show them today's price,

		#return all data, and price 

	def buy(self):
		#number of shares*current price
		#get_info()
		pass
		#Buying should subtract from their funds and not let them buy more than they can afford,

	def sell(self):
		pass

		#selling should return money to their cash funds and not let them sell more than they have.

class User:
		#get username, password, get corresponding data 


	def is_valid(self):
		#check if username and password match

		pass

	def view_dashboard(self):
		pass

		"""users view their portfolio, the amount they have earned or lost, the amount of liquid cash they have available, etc. Make sure they are never looking at stale data. Think of some cool extras - maybe how their portfolio compares to the market average for the year?
		"""
	def create_user(self):
		pass

class Admin:
	def view_leaderboard(self):
		#Create a superuser who can see a leaderboard that displays the top 10 users by portfolio earnings
		#get top 10 users
		#get portfolio earnings

class Account:



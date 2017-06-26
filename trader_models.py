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
    def get_info(self, ticker):
        self.ticker = str(ticker)
        request = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + ticker)
        info = request.json()
        print(info)
        if "LastPrice" in info:
            print(info["LastPrice"])
            return(info["LastPrice"])
        #use API stuff
        #to search companies and get the exact stock ticker symbol we want. 
        #Our users also want to retreive the market data for a stock before they purchase it - we should obviously show them today's price,
        #return all data, and price 
    def buy(self, number):
        number = input("number of shares that the person wants to buy")
        get_info(input("stock they want to buy"))
        Account()
        portfolio_list = []
        total_invested = (number * get_info())
        if account_total - total_invested > 0:
            portfolio_list.append(total_invested)
            account_total = account_total - total_invested 
        else: 
            print("You do not have enough money in your account to complete the transaction.")
        #number of shares*current price
        #get_info()
        pass
        #Buying should subtract from their funds and not let them buy more than they can afford,
    def sell(self, number):
        number = input("number of shares that the person wants to sell")
        input("stock they want to sell")
        total_number_sell = number * get_info()
        Account()
        buy().portfolio_list 
        if total_number_sell < portfolio_list:
            portfolio_list[x] = portfolio_list[x] - total_number_sell
        else:
            print("you do not have enough stocks to sell that amount.")
        account_total = total_number_sell + portfolio_list

class User:
		#get username, password, get corresponding data 
	def __init__(self, user_id= None, username = None, password = None, permission_level = None):
		self.username = username
		self.password = password
		self.user_id = user_id
		self.permission_level = permission_level
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
		self.db_manager.create_client(self.username, self.password)


	def view_dashboard(self):
		dashboard = self.db_manager.view_dashboard(self.username)
		initial_investment = 100,000 - (dashboard["Cash"])
		percent = (dashboard["Portfolio Worth"])/initial_investment
		dashboard["percent earned/lost"] = percent

		return dashboard

		"""users view their portfolio, the amount they have earned or lost, the amount of liquid cash they have available, etc. Make sure they are never looking at stale data. Think of some cool extras - maybe how their portfolio compares to the market average for the year?
		"""



class Account:
	def __init__(self, account_id = None, cash = None, portfolio_worth = None, user_id = None):
		self.account_id = account_id
		self.cash = cash
		self.portfolio_worth = portfolio_worth
		self.user_id = user_id


class Admin: 
	def view_leaderboard(self):
		#Create a superuser who can see a leaderboard that displays the top 10 users by portfolio earnings
		#get top 10 users
		#get portfolio earnings












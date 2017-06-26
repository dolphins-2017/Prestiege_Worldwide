import sqlite3
conn = sqlite3.connect('trader.db')

c = conn.cursor()

from get_lastprice import Markit

class UserDBManager:

	def check_username(self, username):
		c.execute("""SELECT username
			FROM users;""")
		usernames = c.fetchall()
		username_list = [username[0] for username in usernames]
		if username in username_list:
			return True
		else:
			return False

	def check_password(self, username, password):
		querey_list = ["SELECT username, password FROM users WHERE username = '", username, "';"]
		querey_string = "".join(querey_list)

		c.execute(querey_string)
		
		password_in_tuple = c.fetchall()[0][1]
		if password == password_in_tuple:
			return True
		else:
			return False

	def create_client(self, username, password):
		
		c.execute("""INSERT INTO users
			(username, password, permission_level) 
			VALUES 
			(?, ?, ?)
			""",
			(
				username, password, 'client'
					)
		)


		conn.commit()


		querey_lis = ["SELECT id FROM users WHERE username = '", username, "';"]
		querey_str = ''.join(querey_lis)
		c.execute(querey_str)

		client_id = c.fetchall()[0][0]

		c.execute("""INSERT INTO accounts
				(cash, portfolio_worth, user_id) 
				VALUES 
				(?, ?, ?)
				""",
				(
					100000, 0, client_id


				)
			)
		conn.commit()

	def create_admin(self, username, password):
		
		c.execute("""INSERT INTO users
			(username, password, permission_level) 
			VALUES 
			(?, ?, ?)
			""",
			(
				username, password, 'admin'
					)
		)
		conn.commit()


	def find_permission_level(self, username):
		query = "SELECT permission_level FROM users WHERE username = '" + str (username) + "' ;"
		c.execute(query)
		#get class id
		permission_level = (c.fetchall())[0][0]
		return permission_level



	def get_user_id(self,username):
		query = "SELECT id FROM users WHERE username = '" + str (username) + "' ;"
		c.execute(query)
		#get class id
		client_id = (c.fetchall())[0][0]
		return client_id

	def view_account(self, user_id):
		query = "SELECT * FROM accounts WHERE user_id = " + str (user_id) + " ;"
		c.execute(query)
		#get class id

		#list with tuple (id, balance, account_number, user_id )
		return c.fetchall()
	 

	def view_dashboard(self, username):
		query = "SELECT id FROM users WHERE username ='" + str(username) + "' ;"
		c.execute(query)
		user_id = (c.fetchall())[0][0]
		query_ = "SELECT cash, portfolio_worth FROM accounts WHERE user_id = " + str (user_id) + " ;"
		c.execute(query_)
		info = c.fetchall()
		cash = info[0][0]
		portfolio_worth = info[0][1]


		initial_investment = 100000 - cash
		amount = portfolio_worth - initial_investment

		return {"Cash": cash, "Portfolio Worth": portfolio_worth, "Amount earned/lost":amount}

	def view_leaderboard(self):
		query = "SELECT users.username, accounts.portfolio_worth from users INNER JOIN accounts ON users.id = accounts.user_id ORDER BY portfolio_worth DESC LIMIT 10;"

		c.execute(query)
		return c.fetchall





class TransactionsDBManager:
	def buy(self, username, num_shares, ticker, last_price):
		#get user_id
		query = "SELECT id FROM users WHERE username ='" + str(username) + "' ;"
		c.execute(query)
		info = c.fetchall()
		user_id = info[0][0]

		#get cash, portfolio worth
		query_ = "SELECT cash, portfolio_worth, id from accounts WHERE user_id = " + str(user_id) + " ;"
		c.execute(query_)
		info = c.fetchall()
		cash = info[0][0]
		portfolio_worth = info[0][1]
		account_id = info[0][2]


		cost = num_shares * last_price
		new_cash = cash - cost

		#check if user has enough money
		if new_cash < 0:
			return False 

		new_portfolio_worth = portfolio_worth + cost



		#transaction

		c.execute("""INSERT INTO transactions
			(type, account_id, ticker, num_shares)
				VALUES 
				(?, ?, ?, ?)
				""",
				(
					"buy", account_id, ticker, num_shares


					)
				)


		conn.commit()

		#update cash in account
		query2 = "UPDATE accounts SET cash = " + str(new_cash) + " WHERE id = " + str(account_id) + " ;"
		c.execute(query2)
		#update portfolio worth in account
		query3 = "UPDATE accounts SET portfolio_worth = " + str(new_portfolio_worth) + " WHERE id = " + str(account_id) + " ;"
		c.execute(query3)



		# portfolio_list = []
   #      total_invested = (number * get_info())
   #      if account_total - total_invested > 0:
   #          portfolio_list.append(total_invested)
   #          account_total = account_total - total_invested 
   #      else: 
   #          return("You do not have enough money in your account to complete the transaction.")
   #      #number of shares*current price
		#get_info()
	
		#Buying should subtract from their funds and not let them buy more than they can afford,



	def sell(self, username, num_shares, ticker, last_price):
		#get user_id
		query = "SELECT id FROM users WHERE username ='" + str(username) + "' ;"
		c.execute(query)
		info = c.fetchall()
		print(info)
		user_id = info[0][0]

		#get cash, portfolio worth
		query_ = "SELECT cash, portfolio_worth, id from accounts WHERE user_id = " + str(user_id) + " ;"
		c.execute(query_)
		info = c.fetchall()
		cash = info[0][0]
		portfolio_worth = info[0][1]
		account_id = info[0][2]


		cost = num_shares * last_price
		new_cash = cash + cost


		new_portfolio_worth = portfolio_worth - cost



		#transaction

		c.execute("""INSERT INTO transactions
			(type, account_id, ticker, num_shares)
				VALUES 
				(?, ?, ?, ?)
				""",
				(
					"sell", account_id, ticker, num_shares


					)
				)


		conn.commit()

		#update cash in account
		query2 = "UPDATE accounts SET cash = " + str(new_cash) + " WHERE id = " + str(account_id) + " ;"
		c.execute(query2)
		#update portfolio worth in account
		query3 = "UPDATE accounts SET portfolio_worth = " + str(new_portfolio_worth) + " WHERE id = " + str(account_id) + " ;"
		c.execute(query3)



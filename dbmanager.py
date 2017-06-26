import sqlite3
conn = sqlite3.connect('mybank.db')

c = conn.cursor()

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
		query = "SELECT permission_level FROM users WHERE username = " + str (username) + " ;"
		c.execute(query)
		#get class id
		permission_level = (c.fetchall())[0][0]
		return permission_level



	def get_user_id(self,username):
		query = "SELECT id FROM users WHERE username = " + str (username) + " ;"
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
		query = "SELECT id FROM users WHERE username =" + str(username) + " ;"
		c.execute(query)
		user_id = (c.fetchall)[0][0]
		query_ = "SELECT cash, portfolio_worth FROM accounts WHERE user_id = " + str (user_id) + " ;"
		c.execute(query_)
		cash = (c.fetchall)[0][0]
		portfolio_worth = (c.fetchall)[0][1]

		return {"Cash": cash, "Portfolio Worth": portfolio_worth}

	def view_leaderboard(self):
		query = "SELECT users.username, accounts.portfolio_worth from users INNER JOIN accounts ON users.id = accounts.user_id ORDER BY portfolio_worth DESC LIMIT 10;"

		c.execute(query)
		return c.fetchall







class TransactionsDBManager:

	def buy(self, company, how_much):

	def get_balance(self):

		#
	def sell(self):



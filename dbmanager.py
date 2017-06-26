import sqlite3
conn = sqlite3.connect('mybank.db')

c = conn.cursor()

class UserDBManager:
	#conduct sql queries

	"""


	"""

	def check_username(self, username):
		c.execute("""SELECT username
			FROM users;""")
		usernames = c.fetchall()
		username_list = [username[0] for username in usernames]
		if username in username_list:
			return True
		else:
			return False

	def check_password(self):
		querey_list = ["SELECT username, password FROM users WHERE username = '", username, "';"]
		querey_string = "".join(querey_list)

		c.execute(querey_string)
		
		password_in_tuple = c.fetchall()[0][1]
		if password == password_in_tuple:
			return True
		else:
			return False

	def create_client(self):
		
		c.execute("""INSERT INTO users
			(username, password, created_on, permission_level) 
			VALUES 
			(?, ?, ?, ?)
			""",
			(
				username, password, fake.date(), 'client'
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
		


class AccountDBManager:


	def create_account(self, balance, account_number, client_id):

		c.execute("""INSERT INTO accounts
				(balance, account_number, user_id) 
				VALUES 
				(?, ?, ?)
				""",
				(
					balance, account_number, client_id

				))
	def get_account_number (self,username):
		query = "SELECT account_number FROM accounts WHERE username = " + str (username) + " ;"
		c.execute(query)
		#get class id
		account_number = (c.fetchall())[0][0]
		return account_number


	def withdraw(self, account_number, amount):
		query =  "SELECT balance FROM accounts WHERE account_number = " + str (account_number) + " ;"
		c.execute(query)
		#get class id
		balance = int((c.fetchall())[0][0])
		remaining_balance = balance - amount

		query_ = "UPDATE accounts SET balance = " + str(remaining_balance) + " WHERE account_number = " + str(account_number) + " ;"
		c.execute(query_)

		conn.commit()




	def deposit(self, account_number, amount):
		query =  "SELECT balance FROM accounts WHERE account_number = " + str (account_number) + " ;"
		c.execute(query)
		#get class id
		balance = int((c.fetchall())[0][0])
		new_balance = balance + amount

		query_ = "UPDATE accounts SET balance = " + str(new_balance) + " WHERE account_number = " + str(account_number) + " ;"
		c.execute(query_)

		conn.commit()



	def transfer(self, account_from, account_to, amount):

		#withdraw amount from account_to
		query =  "SELECT balance FROM accounts WHERE account_number = " + str (account_from) + " ;"
		c.execute(query)
		#get class id
		balance = int((c.fetchall())[0][0])
		remaining_balance = balance - amount

		query_ = "UPDATE accounts SET balance = " + str(remaining_balance) + " WHERE account_number = " + str(account_from) + " ;"
		c.execute(query_)

		conn.commit()


		#deposit amount into account_to
		query2 =  "SELECT balance FROM accounts WHERE account_number = " + str (account_to) + " ;"
		c.execute(query2)
		#get class id
		balance = int((c.fetchall())[0][0])
		new_balance = balance + amount

		query_2 = "UPDATE accounts SET balance = " + str(new_balance) + " WHERE account_number = " + str(account_to) + " ;"
		c.execute(query_2)

		conn.commit()

class TransactionsDBManager:

	def buy(self, company, how_much):

	def get_balance(self):
	
		#
	def sell(self):



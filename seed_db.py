import sqlite3
from faker import Faker
from random import randint


#change variable names, add transactions table!


def seed_users_table(num_clients,num_admins):
	db = 'trader.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

	print("Destroying old data")
	c.execute("DELETE FROM users")

	fake = Faker()

	for num in range(num_clients):
		c.execute("""INSERT INTO users
			(username, password, permission_level) 
			VALUES 
			(?, ?, ?, ?)
			""",
			(
				fake.user_name(), fake.password(), 'client'
					)
		)
		conn.commit()


	for num in range(num_admins):
		c.execute("""INSERT INTO users
			(username, password, permission_level) 
			VALUES 
			(?, ?, ?, ?)
			""",
			(
				fake.user_name(), fake.password(), 'admin'
					)
		)
		conn.commit()


	#select all user_ids
	c.execute("""SELECT id FROM users WHERE permission_level <> 'admin' ;""")
	#get class ids
	client_ids = c.fetchall()
	#create list of ids
	client_id_list = [info[0] for info in client_ids]
	#print(user_id_list)
	return client_id_list



def seed_accounts_table(client_ids):
	db = 'trader.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

	print("Destroying old data")
	c.execute("DELETE FROM accounts")

	fake = Faker()

	for client_id in client_ids:
		c.execute("""INSERT INTO accounts
				(cash, portfolio_worth, user_id) 
				VALUES 
				(?, ?, ?)
				""",
				(
					100,000, 0, client_id


				)
			)


	conn.commit()

	#select all account_ids
	c.execute("""SELECT id FROM accounts;""")
	#get acount ids
	account_ids = c.fetchall()
	#create list of ids
	account_id_list = [info[0] for info in account_ids]
	
	return account_id_list


# def seed_transactions_table(account_ids):
# 	db = 'trader.db'
# 	conn = sqlite3.connect(db)
# 	c = conn.cursor()

# 	print("Destroying old data")
# 	c.execute("DELETE FROM transactions")

# 	fake = Faker()

# 	for account_id in account_ids:
# 		c.execute("""INSERT INTO accounts
# 				(type, account_id, company_name, amount, timestamp_)
# 				VALUES 
# 				(?, ?, ?)
# 				""",
# 				(
# 					buy/see, 0, client_id


# 				)
# 			)


# 	conn.commit()


def main():
	client_ids = seed_users_table(100, 1)
	account_ids = seed_accounts_table(client_ids)



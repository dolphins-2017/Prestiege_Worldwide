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
			(username, password, created_on, permission_level) 
			VALUES 
			(?, ?, ?, ?)
			""",
			(
				fake.user_name(), fake.password(), fake.date(), 'client'
					)
		)
		conn.commit()


	for num in range(num_bankers):
		c.execute("""INSERT INTO users
			(username, password, created_on, permission_level) 
			VALUES 
			(?, ?, ?, ?)
			""",
			(
				fake.user_name(), fake.password(), fake.date(), 'banker'
					)
		)
		conn.commit()


	#select all user_ids
	c.execute("""SELECT id FROM users WHERE permission_level <> 'banker' ;""")
	#get class ids
	client_ids = c.fetchall()
	#create list of ids
	client_id_list = [info[0] for info in client_ids]
	#print(user_id_list)
	return client_id_list



def seed_accounts_table(client_ids):
	db = 'mybank.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

	print("Destroying old data")
	c.execute("DELETE FROM accounts")

	fake = Faker()

	for client_id in client_ids:
		c.execute("""INSERT INTO accounts
				(balance, account_number, user_id) 
				VALUES 
				(?, ?, ?)
				""",
				(
					randint(0,10000), fake.credit_card_number(), client_id


				)
			)


	conn.commit()

def main():
	client_ids = seed_users_table(100, 5)
	return seed_accounts_table(client_ids)

i

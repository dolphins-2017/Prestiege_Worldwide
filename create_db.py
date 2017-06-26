import sqlite3
conn = sqlite3.connect('trader.db')

c = conn.cursor()


command = "DROP TABLE IF EXISTS users;"
c.execute(command)


c.execute("""CREATE TABLE 'users' (
'id' INTEGER PRIMARY KEY,
'username' VARCHAR,
'password' VARCHAR,
'permission_level' VARCHAR
);""")

conn.commit()

command2 = "DROP TABLE IF EXISTS accounts;"
c.execute(command2)

c.execute("""CREATE TABLE 'accounts' (
'id' INTEGER PRIMARY KEY,
'cash' INTEGER,
'portfolio_worth' INTEGER,
'user_id' INTEGER,
FOREIGN KEY('user_id') REFERENCES users('id')
);""")

conn.commit()

command2 = "DROP TABLE IF EXISTS transactions;"
c.execute(command2)

c.execute("""CREATE TABLE 'transactions' (
'id' INTEGER PRIMARY KEY,
'type' VARCHAR,
'acct_id' INTEGER,
'company_name' VARCHAR,
'amount' INTEGER,
'timestamp_' TIMESTAMP,
FOREIGN KEY('acct_id') REFERENCES accounts('id')
);""")

conn.commit()
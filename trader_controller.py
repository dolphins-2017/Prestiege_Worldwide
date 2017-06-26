import trader_models
import trader_views
import get_lastprice

class Controller:
	def __init__(self):
		view = trader_views.View()
		self.type_ = None

	def type_user():
		type_ = view.type_user()
		self.type = type_

	def new_user:
		#create account
		#check if username is available
		#calls fns in the model
		pass


	def is_valid:
		#check if username/password are valid
		pass
	def main_menu():
		#tidies up input, valid option?
		pass
	def parse_input()
		#EX:	if pick == 'e':
			#self.encrypt()
		#if pick == 'd':
			#self.decrypt()
		#if pick == 'x':
			#self.exit()
			pass
	def buy():
		pass
	def sell():

		pass
	def view_dashboard():
		pass
	def view_leaderboard()
	pass


def main():
	test = Controller()
	user_type = test.type_user()
	if user_type == "n":
		test.new_user()
	elif user_type == "e":
		
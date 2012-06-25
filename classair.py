from webdriverplus import WebDriver  						# New! Need to figure what all I can use it for, but supposed to be Python Friendly
from selenium.webdriver.common.keys import Keys 			# Definitely used for the send_keys(Keys.RETURN) function, send the "Return" key
from selenium.common.exceptions import TimeoutException
from airpass import *										# Stores my passwords for logins
import re 													# imports regex, not using currently
import datetime												# used to get the current time
import getpass												# for security purposes, user cannot see the password being entered

lines_spaces = '-' * 150
#||||||||||||||||||||||||||||||||||Beginning of Class Definitions||||||||||||||||||||||||||||||||||||||||||||||||
class AirlineMiles(object):
	"""Contains all the attributes that is necessary for finding airline miles"""

	def __init__(self, driver):
	 	self.driver = driver

	def get_url(self, award_url):
		# go to the Airline Miles Web page
		self.driver.get(award_url)
	
	def enter_user_name(self, user_name):
		for e in self.driver.find('input'):
			#print e.id
			if re.search("email|aadvantageNumber|UserId|username", e.id, flags=re.I):
				user_name_path = e.id

		# find the element that's name attribute is Email (username box)
		user_name_box = self.driver.find(id=user_name_path)
		# type in the user name
		user_name_box.send_keys(user_name)

	def enter_user_password(self, user_password):
		for e in self.driver.find('input'):
			#print e.id
			if re.search("password|pwd", e.id, flags=re.I):
				user_password_path = e.id
		
		# find the element that's name attribute is password (the password box)
		password_box = self.driver.find(id=user_password_path)
		# type in the password
		password_box.send_keys(user_password,"\n")	# submit the form with the '\n'

	def get_mileage_balance(self):
		array = []
		for e in self.driver.find('div'):
			if re.search("\d+,?\d*\s*pts", e.text, flags= re.I):
				mileage_balance = re.search("(\d+,?\d*)\s*pts", e.text, flags= re.I).group(1)
			if re.search("(?:Balance:|Miles:)\s*(\d+,?\d*)", e.text, flags=re.I):
				mileage_balance = re.search("(?:Balance:|Miles:)\s*(\d+,?\d*)", e.text, flags=re.I).group(1)

		print mileage_balance
		print lines_spaces

#||||||||||||||||||||||||||||||||||Beginning of Function Definitions||||||||||||||||||||||||||||||||||||||||||||||||
def current_time():
	now = datetime.datetime.now()
	print "Current date and time"
	print "%d-%d-%d %d:%d" % (now.day, now.month, now.year, now.hour, now.minute)

def get_miles(driver, url, user, password):
	airline_miles = AirlineMiles(driver)
	airline_miles.get_url(url)
	airline_miles.enter_user_name(user)
	airline_miles.enter_user_password(password)
	return airline_miles.get_mileage_balance()

# get_miles(driver, jetblue_url, me['jetblue_user'], me['jet_blue_pass'])

# jet_blue = (driver, jetblue_url, me['jetblue_user'], me['jet_blue_pass'])

# get_miles(*jet_blue)
# get_miles(**jet_blue_dict)

# def wait_for_element(e, timeout=60):
# 	pass

# wait_for_element(e)

# wait_for_element(e, 30)

# class Foo(Bar):

# 	def __init__(self, foo_p, *args, **kwargs):
# 		self.foo_p = foo_p
# 		super(Foo, self).__init__(*args, **kwargs)



# jet_blue_dict = {"driver": driver, "url": }
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Beginning of Program$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
me = {'name': 'Brian', 'jetblue_user': 'balexander04@gmail.com', 'jet_blue_pass': jet_blue_pass, 
	'aadvantage_user': '132AEU6', 'aadvantage_pass': aadvantage_pass,
	'alaska_air_user': '108970153', 'alaska_air_pass': alaska_air_pass }

# Create a new instance of the Firefox driver
driver = WebDriver('firefox', quit_on_exit=True, reuse_browser=True)


#Award airlineMile URL's
jetblue_url = "https://book.jetblue.com/B6.auth/login?intcmp=hd_signin&service=https://www.jetblue.com/default.aspx"
american_air_url = "https://www.aa.com/login/loginAccess.do?uri=%2flogin%2floginAccess.do&previousPage=%2fhomePage.do&bookingPathStateId=&marketId="
alaska_air = "https://www.alaskaair.com/www2/ssl/myalaskaair/MyAlaskaAir.aspx?CurrentForm=UCSignInStart&url=https://www.alaskaair.com/www2/ssl/myalaskaair/MyAlaskaAir.aspx?"

print "Jet Blue"
jetblue = AirlineMiles(driver)
jetblue.get_url(jetblue_url)
jetblue.enter_user_name(me['jetblue_user'])
jetblue.enter_user_password(me['jet_blue_pass'])
jetblue.get_mileage_balance()
# print "Press enter for next!"
# raw_input()



#get_miles(jetblue)

print "Alaska Air"
american_air = AirlineMiles(driver)
american_air.get_url(american_air_url) 
american_air.enter_user_name(me['aadvantage_user'])
american_air.enter_user_password(me['aadvantage_pass'])
american_air.get_mileage_balance()
# print "Press enter for next!"
# raw_input()

print "American Airlines"
alaskaair = AirlineMiles(driver)
alaskaair.get_url(alaska_air)
alaskaair.enter_user_name(me['alaska_air_user'])
alaskaair.enter_user_password(me['alaska_air_pass'])
alaskaair.get_mileage_balance()

print "Press enter to close!"
raw_input()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 			# Definitely used for the send_keys(Keys.RETURN) function, send the "Return" key
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 	        # available since 2.4.0
import datetime								# used to get the current time
import getpass								# for security purposes, user cannot see the password being entered
import re


#||||||||||||||||||||||||||||||||||Beginning of Function Definitions||||||||||||||||||||||||||||||||||||||||||||||||
def current_time():
	now = datetime.datetime.now()
	print "Current date and time"
	print "%d-%d-%d %d:%d" % (now.day, now.month, now.year, now.hour, now.minute)
	
def enter_user_name(user_name_path, user_name):
	# find the element that's name attribute is Email (username box)
	user_name_box = WebDriverWait(driver, 2).until(lambda driver : driver.find_element_by_name(user_name_path))
	# type in the user name
	user_name_box.send_keys(user_name)
	
def enter_password(password_box_path, password):
	# find the element that's name attribute is password (the password box)
	password_box = WebDriverWait(driver, 1).until(lambda driver : driver.find_element_by_name(password_box_path))
	# type in the password
	password_box.send_keys(password)
	# submit the form
	password_box.send_keys(Keys.RETURN)

def print_available_miles(xpath):
	available_miles = WebDriverWait(driver, 5).until(lambda driver : driver.find_element_by_xpath(xpath).text)
	return available_miles

def enter_origin_city_name(origin_city_path):
	origin_city_box = WebDriverWait(driver, 4).until(lambda driver : driver.find_element_by_id(origin_city_path))
	origin_city_box.click()
	origin_city_box.send_keys("AUS")
	return origin_city_box

def enter_destination_city_name(destination_city_path):
	destination_city_box = WebDriverWait(driver, 2).until(lambda driver : driver.find_element_by_id(destination_city_path))
	destination_city_box.click()
	destination_city_box.send_keys("SFO")
	return destination_city_box

def print_departure_flight_miles(xpath):
	departure_flight = WebDriverWait(driver, 6).until(lambda driver : driver.find_element_by_xpath(xpath))
	departure_flight = re.search("(\d+\,?\d+)", departure_flight.text).group(1)
	print "Departure Flight: %s" % departure_flight

def print_return_flight_miles(xpath):
	return_flight = WebDriverWait(driver, 4).until(lambda driver : driver.find_element_by_xpath(xpath))
	return_flight = re.search("(\d+\,?\d+)", return_flight.text).group(1)
	print "Return Flight: %s" % return_flight
	
def jet_blue_sign_on():
	# go to the JetBlue Web page
	driver.get("https://www.jetblue.com")
	
	assert "JetBlue" in driver.title

	# go to the JetBlue TrueBlue SignIn page
	'''sign_in_button_path = "sign-in"
	sign_in_button = driver.find_element_by_class_name(sign_in_button_path)
	sign_in_button.click()'''
        
	# finds the username box and then sends keys to type out the username
	jet_blue_user_path = "ctl00$Content$TrueBlueMode$LoggedOutMode$email_field"
	jet_blue_user = "balexander04@gmail.com"
	enter_user_name(jet_blue_user_path, jet_blue_user)

	# finds the password box and then sends keys to type out the password
	jet_blue_pass_path = "ctl00$Content$TrueBlueMode$LoggedOutMode$password_field"
	jet_blue_pass = getpass.getpass("What is your jetblue password?")
	enter_password(jet_blue_pass_path, jet_blue_pass)
	
	points_available_path = "/html/body/div[4]/div/div[2]/ul/li[6]/a/span[2]"
	print "Available Points:", print_available_miles(points_available_path)
	
def jet_blue_search():
        # go to the airline's book flight page
        driver.get("http://jetblue.com/flights/?intcmp=hd_plan_flights")

        origin_city_path = "originAirportsDisplay"
        origin_city_box = enter_origin_city_name(origin_city_path)
        origin_city_box.send_keys(Keys.RETURN)

        destination_city_path = "destinationAirportsDisplay"
        destination_city_box = enter_destination_city_name(destination_city_path)
        destination_city_box.send_keys(Keys.RETURN)

        next_date = driver.find_element_by_link_text("Next Month (March 2012)")
        next_date.click()
        next_date = driver.find_element_by_link_text("Next Month (April 2012)")
        next_date.click()

        departure_date = driver.find_element_by_xpath("/html/body/div[10]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a")
        departure_date.click()

        return_date = driver.find_element_by_xpath("/html/body/div[9]/div/div[2]/div/div/table/tbody/tr[3]/td/a")
        return_date.click()

        points_radio_button = driver.find_element_by_id("fareTypeTrueblue")  
        points_radio_button.click()

        find_flights = driver.find_element_by_id("searchFormSubmit")
        find_flights.click()

        #outbound_fare = driver.find_element_by_name("outbound_fare")
        #outbound_fare.click()

        departure_flight_path = '/html/body/div[9]/div[2]/div/form/div/div[2]/ul/li[4]/div/div/span'
        print_departure_flight_miles(departure_flight_path)

        return_flight_path = '/html/body/div[9]/div[2]/div/form/div/div[6]/ul/li[4]/div/div/span'
        print_return_flight_miles(return_flight_path)

def alaska_air_sign_on():
	# go to the Alaska Air Member Area SignIn page
	driver.get("https://www.alaskaair.com/www2/ssl/myalaskaair/MyAlaskaAir.aspx?CurrentForm=UCSignInStart&url=https://www.alaskaair.com/www2/ssl/myalaskaair/MyAlaskaAir.aspx?")
	
	# finds the username box and then sends keys to type out the username
	alaska_air_user_path = "FormUserControl$_signInProfile$_userIdControl$_userId"
	alaska_air_user = "108970153"
	enter_user_name(alaska_air_user_path, alaska_air_user)
	
	# finds the password box and then sends keys to type out the password
	alaska_air_pass_path = "FormUserControl$_signInProfile$_passwordControl$_password"
	alaska_air_pass = getpass.getpass("What is your alaskaair password?")
	enter_password(alaska_air_pass_path, alaska_air_pass)

	available_miles_path = '//*[@id="FormUserControl__myOverview__mileagePlanInfo"]'
	print print_available_miles(available_miles_path)

def alaska_air_search():
	# go to the airline's book flight page
	driver.get("http://www.alaskaair.com/planbook?lid=nav:planbook")
	
	origin_city_path = "fromCity"
	enter_origin_city_name(origin_city_path)
	
	departing_date = driver.find_element_by_id("departureDate")
	departing_date.clear()
	departing_date.send_keys("04/11/2012")
	
	destination_city_path = "toCity"
	enter_destination_city_name(destination_city_path)
	
	returning_date = driver.find_element_by_id("returnDate")
	returning_date.clear()
	returning_date.send_keys("04/15/2012")
	
	award_flight = driver.find_element_by_id("awardReservation")
	award_flight.click()
	
	award_calendar = driver.find_element_by_id("awardCalendar")
	award_calendar.click()
	award_calendar.send_keys(Keys.RETURN)
	
	departure_flight_path = '//*[@id="SelectedFare_adt0"]'
	print_departure_flight_miles(departure_flight_path)
	
	return_flight_path = '//*[@id="SelectedFare_adt1"]'
	print_return_flight_miles(return_flight_path)

def american_airlines_sign_on():
	# go to the AAdvantage Member SignIn page
	driver.get("https://www.aa.com/login/loginAccess.do?uri=/login/loginAccess.do&previousPage=/myAccount/reservationPreferencesAccess.do&continueUrl=/myAccount/reservationPreferencesAccess.do&v_locale=en_US&v_mobileUAFlag=AA&previousPage=/myAccount/reservationPreferencesAccess.do&uri=/login/loginAccess.do&continueUrl=/myAccount/reservationPreferencesAccess.do")

	# finds the username box and then sends keys to type out the username
	aadvantage_user_path = "aadvantageNumber"
	aadvantage_user = "132AEU6"
	enter_user_name(aadvantage_user_path, aadvantage_user)
	
	# finds the password box and then sends keys to type out the password
	aadvantage_pass_path = "password"
	aadvantage_pass = getpass.getpass("What is your aadvantage password?")
	enter_password(aadvantage_pass_path, aadvantage_pass)

	available_miles_path = '/html/body/div/div/div[3]/p'
	print print_available_miles(available_miles_path)

def american_airlines_search():
	# go to the airline's book flight page
	driver.get("https://www.aa.com/reservation/awardFlightSearchAccess.do?anchorEvent=false&from=Nav")

	origin_city_path = "awardFlightSearchForm.originAirport"
	enter_origin_city_name(origin_city_path)
	
	destination_city_path = "awardFlightSearchForm.destinationAirport"
	enter_destination_city_name(destination_city_path)
	
	#Departure Flight Date
	#Specific month of departure
	departure_date_month = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div/select/option[4]")
	departure_date_month.click()
	#Specific day of departure
	departure_date_day = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div/select[2]/option[11]")
	departure_date_day.click()
	#Specific 'time of day' of departure
	departure_date_time = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div/select[3]/option")
	departure_date_time.click()
	
	#Return Flight Date
	#Specific day of return
	return_date_month = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div[2]/select/option[4]")
	return_date_month.click()
	#Specific day of return
	return_date_day = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div[2]/select[2]/option[15]")
	return_date_day.click()
	#Specific 'time of day' of return
	return_date_time = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/table/tbody/tr[4]/td/form/table/tbody/tr/td/div/div/div/div[5]/div[2]/div[2]/select[3]/option")
	return_date_time.click()
	
	#Select the button and click it to submit the form
	go_button_element = driver.find_element_by_id("awardFlightSearchForm.button.go")
	go_button_element.click()
	
	#Capture and store the value of miles required for the submitted departure date
	departure_flight_path = '//*[@id="flightTabMiles_0"]'
	print_departure_flight_miles(departure_flight_path)
	
	#Capture and store the value of miles required for the submitted return date
	return_flight_path = '//*[@id="flightTabMiles_1"]'
	print_return_flight_miles(return_flight_path)
	
	
#||||||||||||||||||||||||||||||||||End of Function Definitions||||||||||||||||||||||||||||||||||||||||||||||||

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Beginning of Program$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

current_time()
print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||"

print "Jet Blue"
#jet_blue_sign_on()
print "-------------------------------------------------------"
#jet_blue_search()
print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||"

print "Alaska Air"
#alaska_air_sign_on()
print "-------------------------------------------------------"
#alaska_air_search()
print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||"

print "American Airlines"
american_airlines_sign_on()
print "-------------------------------------------------------"
#american_airlines_search()
print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||"

print "Press enter to close!"
raw_input()
driver.quit()


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$End of Program$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

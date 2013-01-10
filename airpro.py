import re
from sys import argv
from time import sleep

from webdriverplus import WebDriver

# import script
import util
from airpass import *  # Stores my passwords for logins


lines_spaces = '-' * 150
month = 'January'
year = '2013'
dept_day = '8'
arr_day = '15'


class AIRLINE_MILES(object):
    '''docstring for AIRLINE_MILES
       Class that retrieves Airline miles
       by logging in to the company chosen'''

    def __init__(self, driver=None):
        super(AIRLINE_MILES, self).__init__()
        self.__driver = driver

    def run_all(self):
        for klass in [AMERICAN_AIR, ALASKA_AIR, JET_BLUE][:1]:
            file_name = klass().name + '.html'
            print lines_spaces, '\n', klass().name
            self.open_url(klass().URL)
            # self.enter_user_name(klass().user_name)
            # self.enter_user_password(klass().password)
            # self.get_mileage_balance()
            if not self.find_flight_search_page(file_name):
                print 'Did not Find Reservations Page'
            klass().flight_search()

    def open_url(self, URL):
        self.driver.get(URL)

    def find_flight_search_page(self, file_name):
        '''Looks for a link on the page to navigate to search page'''
        print 'searching for reservations page'
        for e in self.driver.find('a'):
            if re.search(r'^Reservations|PLAN \& BOOK|Plan a trip$', e.text):
                print 'Found Reservations Page'
                e.click()
                return True
        return False

    def enter_user_name(self, user_name):
        '''Find input box for user name, then input user name'''
        for e in self.driver.find('input'):
            if re.search("email|loginId|UserId|username", e.id, flags=re.I):
                user_name_path = e.id
        # find the element that's name attribute is Email (username box)
        user_name_box = self.driver.find(id=user_name_path)
        # type in the user name
        user_name_box.send_keys(user_name)

    def enter_user_password(self, user_password):
        '''Find input box for password, then input password'''
        for e in self.driver.find('input'):
            if re.search("password|pwd", e.id, flags=re.I):
                user_password_path = e.id
        # find the element that's name attribute is password (the password box)
        password_box = self.driver.find(id=user_password_path)
        # type in the password
        password_box.send_keys(user_password, "\n")  # submit form with the'\n'

    def get_mileage_balance(self):
        '''Find the amount of miles on the page'''
        sleep(5)
        page = util.create_page(self.driver)
        try:
            if page.xpath('//span[@class="points"]'):
                mileage_balance = page.xpath('//span[@class="points"]'
                                  )[0].text_content().strip('\n pts.')
            elif page.xpath('//th'):
                mileage_balance = page.xpath('//th')[0].text.strip('\n ')
            elif page.xpath('.//div[@id="FormUserControl__'
                            'myOverview__mileagePlanInfo"]'):
                header = page.xpath('.//div[@id="FormUserControl__'
                                    'myOverview__mileagePlanInfo"]'
                                    )[0].text_content()
                mileage_balance = re.search(r'Miles:(.+$)',
                                  header).group(1).replace(u'\xa0', u'')
            print mileage_balance
        except:
            pass

    def save_flight(self, file_name):
        '''Chea chea chae'''
        page = util.create_page_from_file(file_name)
        print page
        sleep(3)
        page = util.create_page(self.driver)
        util.save_page(page, file_name)

    def type_depart_city(self):
        for e in self.driver.find('input'):
            if re.search('origin', e.id):
                e.send_keys('AUS')
                break

    def type_arrival_city(self):
        for e in self.driver.find('input'):
            if re.search('destination', e.id):
                e.send_keys('LAS')
                break

    @property
    def driver(self):
        if self.__driver is None:
            self.__driver = WebDriver('firefox',
            quit_on_exit=True, reuse_browser=True)
        return self.__driver


class ALASKA_AIR(object):
    """docstring for ALASKA_AIR
       Class for Alaska Airlines"""

    def __init__(self):
        super(ALASKA_AIR, self).__init__()
        self.driver = AIRLINE_MILES().driver
        self.name = 'Alaska Airlines'
        self.user_name = '108970153'
        self.password = alaska_air_pass
        self.URL = ('https://www.alaskaair.com'
                    '/www2/ssl/myalaskaair/MyAlaskaAir.aspx?'
                    'CurrentForm=UCSignInStart&url=https://www'
                    '.alaskaair.com/www2/ssl/myalaskaair/MyAlas'
                    'kaAir.aspx?')

    def flight_search(self):
        # go to the airline's book flight page
        pass


class AMERICAN_AIR(object):
    """docstring for AMERICAN_AIR
       Class for American Airlines"""

    def __init__(self):
        super(AMERICAN_AIR, self).__init__()
        self.driver = AIRLINE_MILES().driver
        self.name = 'American Airlines'
        self.user_name = '132AEU6'
        self.password = aadvantage_pass
        self.URL = ('https://www.aa.com/login'
                    '/loginAccess.do?uri=%2flogin%2floginAccess'
                    '.do&previousPage=%2fhomePage.do&'
                    'bookingPathStateId=&marketId=')

    def flight_search(self):
        # go to the airline's book flight page
        # AIRLINE_MILES().type_depart_city()
        AIRLINE_MILES().type_arrival_city()
        # Departure Flight Date
        # Specific month of departure
        depart_month_select = self.driver.find(name='flightParams.'
                                        'flightDateParams.travelMonth')
        [e.click() for e in depart_month_select.find('option')
                       if e.value == '5']
        # Specific day of departure
        depart_day_select = self.driver.find(name='flightParams.'
                                             'flightDateParams.travelDay')

        [e.click() for e in depart_day_select.find('option')
                       if e.value == '17']
        # Specific 'time of day' of departure
        depart_time = self.driver.find(name='flightParams.'
                                       'flightDateParams.searchTime')[0]
        [e.click() for e in depart_time.find('option') if e.value == '120001']

        # Arrival Flight Date
        # Specific month of return
        return_month_select = self.driver.find(id='returnMonth')
        [e.click() for e in return_month_select.find('option')
                       if e.value == '5']
        # Specific day of return
        return_day_select = self.driver.find(id='returnDay')

        [e.click() for e in return_day_select.find('option')
                       if e.value == '22']
        # Specific 'time of day' of departure
        return_time = self.driver.find(id='returnYear')
        [e.click() for e in return_time.find('option') if e.value == '120001']

        # Select check box to redeem miles
        self.driver.find(value="award").click()
        # Select the button and click it to submit the form
        self.driver.find(id="flightSearchForm.button.reSubmit").click()


class JET_BLUE(object):
    """docstring for JET_BLUE
       Class for Jet Blue"""

    def __init__(self):
        super(JET_BLUE, self).__init__()
        self.driver = AIRLINE_MILES().driver
        self.name = 'Jet Blue'
        self.user_name = 'balexander04@gmail.com'
        self.password = jet_blue_pass
        self.URL = ('https://book.jetblue.com/'
                    'B6.auth/login?intcmp=hd_signin&service='
                    'https://www.jetblue.com/default.aspx')

    def flight_search(self):
        # go to the airline's book flight page
        pass

if __name__ == '__main__':
    try:
        if argv[1] == 'aa':
            pass
    except IndexError:
        AIRLINE_MILES().run_all()

print lines_spaces
raw_input('end of program')

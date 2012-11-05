import re
import time

import script
import util


lines_spaces = '-' * 150


class AirlineMiles(script.Script):

    def __init__(self):
        super(AirlineMiles, self).__init__('https://book.jetblue.com/B6.auth/'
                                     'login?intcmp=hd_signin&service='
                                     'https://www.jetblue.com/default.aspx')

    def do_stuff(self):
        for airline, password, user, link in zip(self.airline_name,
                                                 self.user_pass,
                                                 self.user_name,
                                                 self.airlinemile_links):
            print lines_spaces
            print airline
            self.driver.get(self.airlinemile_links[link])
            self.enter_user_name(self.user_name[user])
            self.enter_user_password(self.user_pass[password])
            self.get_mileage_balance()
            self.search_flight()
        raw_input('end')

    def enter_user_name(self, user_name):
        '''Find input box for user name, then input user name'''
        for e in self.driver.find('input'):
            if re.search("email|aadvantageNumber|UserId|username", e.id, flags=re.I):
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
        password_box.send_keys(user_password, "\n")  # submit the form with the '\n'

    def get_mileage_balance(self):
        '''Find the amount of miles on the page'''
        time.sleep(5)
        page = util.create_page(self.driver)
        try:
            if page.xpath('//span[@class="points"]'):
                mileage_balance = page.xpath('//span[@class="points"]')[0].text_content().strip('\n pts.')
            elif page.xpath('//th'):
                mileage_balance = page.xpath('//th')[0].text.strip('\n ')
            elif page.xpath('.//div[@id="FormUserControl__myOverview__mileagePlanInfo"]'):
                header = page.xpath('.//div[@id="FormUserControl__myOverview__mileagePlanInfo"]')[0].text_content()
                mileage_balance = re.search(r'Miles:(.+$)', header).group(1).replace(u'\xa0', u'')
            print mileage_balance
        except:
            pass

    def search_flight(self):
        '''Takes Departure, and Arrival location with
        dates and searches for flights'''
        print self.URL

if __name__ == '__main__':
    AirlineMiles().do_stuff()

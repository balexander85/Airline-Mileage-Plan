from webdriverplus import WebDriver
from airpass import *  # Stores my passwords for logins


class Script(object):

    def __init__(self, driver=None):
        self.__driver = driver
        self.airline_name = {'jet_blue': 'Jet Blue', 'american_air': 'American Airlines',
                             'alaska_air': 'Alaska Airlines'}
        self.user_name = {'jet_blue': 'balexander04@gmail.com',
                     'american_air': '132AEU6',
                     'alaska_air': '108970153'}
        self.user_pass = {'jet_blue': jet_blue_pass,
                          'american_air': aadvantage_pass,
                          'alaska_air': alaska_air_pass}
        self.airlinemile_links = {'jet_blue': 'https://book.jetblue.com/'
                                   'B6.auth/login?intcmp=hd_signin&service='
                                   'https://www.jetblue.com/default.aspx',
                                   'american_air': 'https://www.aa.com/login'
                                   '/loginAccess.do?uri=%2flogin%2floginAccess'
                                   '.do&previousPage=%2fhomePage.do&'
                                   'bookingPathStateId=&marketId=',
                                   'alaska_air': 'https://www.alaskaair.com/'
                                   'www2/ssl/myalaskaair/MyAlaskaAir.aspx?'
                                   'CurrentForm=UCSignInStart&url=https://www'
                                   '.alaskaair.com/www2/ssl/myalaskaair/MyAlas'
                                   'kaAir.aspx?'}

    @property
    def driver(self):
        if self.__driver is None:
            self.__driver = WebDriver('firefox',
            quit_on_exit=True, reuse_browser=True)
        return self.__driver

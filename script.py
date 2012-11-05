from webdriverplus import WebDriver
from airpass import *  # Stores my passwords for logins


class Script(object):

    def __init__(self, url, driver=None):
        self.__driver = driver
        self.URL = url
        self.airline_name = ('Jet Blue', 'American Airlines',
                             'Alaska Airlines')
        self.user_name = {'1jetblue_user': 'balexander04@gmail.com',
                     '2aadvantage_user': '132AEU6',
                     '3alaska_air_user': '108970153'}
        self.user_pass = {'1jet_blue_pass': jet_blue_pass,
                          '2aadvantage_pass': aadvantage_pass,
                          '3alaska_air_pass': alaska_air_pass}
        self.airlinemile_links = {'1jet_blue': 'https://book.jetblue.com/'
                                   'B6.auth/login?intcmp=hd_signin&service='
                                   'https://www.jetblue.com/default.aspx',
                                   '2american_air': 'https://www.aa.com/login'
                                   '/loginAccess.do?uri=%2flogin%2floginAccess'
                                   '.do&previousPage=%2fhomePage.do&'
                                   'bookingPathStateId=&marketId=',
                                   '3alask_air': 'https://www.alaskaair.com/'
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

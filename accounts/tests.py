from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class AccountsViewTests(LiveServerTestCase):
    fixtures = ['user_dump.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        super(AccountsViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(AccountsViewTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.assertEquals(u'ログイン', self.selenium.title)

        username_input = self.selenium.find_element_by_name('login')
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('test')
        self.selenium.find_element_by_xpath('//form[button/@type="submit"]').click()

    def test_signup(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        self.assertEquals(u'ユーザー登録', self.selenium.title)

        username_input = self.selenium.find_element_by_name('username')
        email_input = self.selenium.find_element_by_name('email')
        password_input = self.selenium.find_element_by_name('password1')
        password2_input = self.selenium.find_element_by_name('password2')

        username_input.send_keys('testuser')
        email_input.send_keys('test@example.com')
        password_input.send_keys('testpassword')
        password2_input.send_keys('testpassword')
        self.selenium.find_element_by_xpath('//form[button/@type="submit"]').click()
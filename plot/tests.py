from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver 


class PlotViewTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(PlotViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(PlotViewTests, cls).tearDownClass()

    def test_get_index(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/'))
        self.assertEquals(u'プロットをよもう。かこう。 - Plothub', self.selenium.title)

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.assertEquals(u'ログイン', self.selenium.title)

        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('test')
        self.selenium.find_element_by_class_name('button is-success primaryAction').click()

        self.assertEquals(u'', self.selenium.title)

    def test_signup(self):
        pass

    def test_create(self):
        pass

    def test_delete(self):
        pass

    def test_edit(self):
        pass
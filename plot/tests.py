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

    def test_create(self):
        pass

    def test_delete(self):
        pass

    def test_edit(self):
        pass
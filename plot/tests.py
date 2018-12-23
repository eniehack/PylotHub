from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


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
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/new/'))
        self.selenium.implicitly_wait(10)
        self.assertEquals(u'プロットの新規作成 - PlotHub', self.selenium.title)

        title_input = self.selenium.find_element_by_name('title')
        genre_element = self.selenium.find_element_by_name('genre')
        genre_select_element = Select(genre_element)
        content_input = self.selenium.find_element_by_name('content')

        title_input.send_keys('test')
        genre_select_element.select_by_value('01')
        content_input.send_keys('これはSeleniumを使ったテストです')

        self.selenium.find_elements_by_class_name('button is-primary').click()
        self.selenium.implicitly_wait(10)
        self.assertEquals('have created your new post!', self.selenium.find)

    def test_delete(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/search/'))
        self.selenium.implicitly_wait(10)
        self.assertEquals(u'プロット検索 - PlotHub', self.selenium.title)

        self.selenium.find_elements_by_class_name('detail_link').click()
        self.selenium.implicitly_wait(10)

        self.selenium.find_elements_by_class_name('button is-danger').click()
        self.selenium.implicitly_wait(10)
        self.assertEquals(u'プロットの削除 - PlotHub', self.selenium.title)

    def test_edit(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/search/'))
        self.selenium.implicitly_wait(10)
        self.assertEquals(u'プロット検索 - PlotHub', self.selenium.title)

        self.selenium.find_elements_by_class_name('detail_link').click()
        self.selenium.implicitly_wait(10)

        self.selenium.find_elements_by_class_name('button is-link').click()
        self.selenium.implicitly_wait(10)
        self.assertEquals(u'プロットの編集 - PlotHub', self.selenium.title)

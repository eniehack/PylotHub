from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlotViewTests(LiveServerTestCase):
    fixtures = ['plot_dump.json', 'user_dump.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(PlotViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(PlotViewTests, cls).tearDownClass()
    
    def login(self, redirect_for):
        self.selenium.get('%s%s%s' % (self.live_server_url, '/accounts/login/?next=', redirect_for))
        username_input = self.selenium.find_element_by_id('id_login')
        password_input = self.selenium.find_element_by_id('id_password')
        username_input.send_keys('testuser')
        password_input.send_keys('testpassword')
        self.selenium.find_element_by_xpath('//form[button/@class="button is-success primaryAction"]')

    def test_get_index(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/'))
        self.assertEquals(u'プロットをよもう。かこう。 - Plothub', self.selenium.title)

    def test_create_not_authenticated(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/new/'))
        self.assertEquals(u'ログイン', self.selenium.title)

    def test_create(self):
        self.login('/plots/new/')
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, 'textarea#id_content')))
        self.assertEquals(u'プロットの新規作成 - PlotHub', self.selenium.title)

        title_input = self.selenium.find_element_by_name('title')
        genre_element = self.selenium.find_element_by_name('genre')
        genre_select_element = Select(genre_element)
        content_input = self.selenium.find_element_by_name('content')

        title_input.send_keys('test')
        genre_select_element.select_by_value('01')
        content_input.send_keys('これはSeleniumを使ったテストです')

        self.selenium.find_element_by_xpath('//form[button/@type="submit"]').click()

    def test_delete_not_authenticated(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/8273ef14-fb31-4bb6-8bf2-da1da066e718/delete'))
        self.assertEquals('403 Forbidden', self.selenium.find_element_by_css_selector('h1').text)

    def test_delete(self):
        self.login('/plots/8273ef14-fb31-4bb6-8bf2-da1da066e718/delete')
        WebDriverWait(self.selenium, 10).until(EC.element_to_be_clickable((By.XPATH, '//form[button/@class="button is-danger"]')))
        self.assertEquals(u'プロットの削除 - PlotHub', self.selenium.title)

        self.selenium.find_elements_by_xpath('//form[button/@type="submit"]').click()

    def test_edit_not_authenticated(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/plots/57abdc1a-598f-4ecd-9b26-7c20cacaed34/edit'))
        self.assertEquals('403 Forbidden', self.selenium.find_element_by_css_selector('h1').text)

    def test_edit(self):
        self.login('/plots/57abdc1a-598f-4ecd-9b26-7c20cacaed34/edit')
        wait = WebDriverWait(self.selenium, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea#id_content')))
        print(element)
        self.assertEquals(u'プロットの編集 - PlotHub', self.selenium.title)

        self.selenium.find_elements_by_xpath('//form[button/@type="submit"]').click()
        

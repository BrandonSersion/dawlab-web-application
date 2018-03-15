from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException

import os

MAX_WAIT = 10  

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()  
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

class LayoutAndStylingTest(FunctionalTest):

    def test_home_layout_and_styling(self):
        #User visits home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        #User sees the page load
        assert 'DAWLAB Software' in self.browser.title

        #User sees the nav, h1, and footer elements
        self.browser.find_element_by_tag_name('nav')
        self.browser.find_element_by_tag_name('h1')
        self.browser.find_element_by_tag_name('footer')

        #User sees the correct bootstrap theme
        navbar_background_color = self.browser.find_element_by_tag_name('nav').value_of_css_property("background-color")
        self.assertEqual(navbar_background_color, 'rgb(52, 58, 64)')

        #CURRENTLY BROKEN User sees the correct static images
        # img_from_page = self.browser.find_element_by_tag_name('img').get_attribute('size')
        # img_from_file = os.path.join(os.path.dirname(__file__), '../content/static/img/Ali.jpg')
        # self.assertEqual(img_from_page, img_from_file)

        #User sees the header in Arial or Times font
        h1_font_from_page = self.browser.find_element_by_tag_name('h1').value_of_css_property("font-family")
        self.assertEqual(h1_font_from_page, '"Arial", Times, serif')

    def test_our_team_layout_and_styling(self):
        page_url = '/our_team.html'
        #User visits home page.
        self.browser.get(self.live_server_url + page_url)
        self.browser.set_window_size(1024, 768)

        #User sees home page title
        assert 'DAWLAB Software' in self.browser.title

        #User sees the nav, h1, and footer elements
        self.browser.find_element_by_tag_name('nav')
        self.browser.find_element_by_tag_name('h1')
        self.browser.find_element_by_tag_name('footer')

        #User sees the correct bootstrap theme
        navbar_background_color = self.browser.find_element_by_tag_name('nav').value_of_css_property("background-color")
        self.assertEqual(navbar_background_color, 'rgb(52, 58, 64)')

        #CURRENTLY BROKEN User sees the correct static images
        # img_from_page = self.browser.find_element_by_tag_name('img').get_attribute('size')
        # img_from_file = os.path.join(os.path.dirname(__file__), '../content/static/img/Ali.jpg')
        # self.assertEqual(img_from_page, img_from_file)

        #User sees the header in Arial or Times font
        h1_font_from_page = self.browser.find_element_by_tag_name('h1').value_of_css_property("font-family")
        self.assertEqual(h1_font_from_page, '"Arial", Times, serif')



# class AuthenticationTest(FunctionalTest):

#     def test_authentication(self):









    #USER TESTS
    
    #User loads webpage, sees all page assets

    #User x'es out newsletter popup

    #OR User submits email to newsletter popup, gets feedback that it went through

    #User clicks on employee area, is denied access

    #User visits on a tablet 

    #User visits on a cell phone


    #EMPLOYEE TESTS

    #Employee inputs username and password, is admitted to employee area

    #OR Employee uses 'forgot password' option, it works

    #Employee sees the latest company announcement

    #Employee pages through past announcements

    #Messenger alerts employee of unread messenges - employee views those messenges

    #Employee views whole inbox

    #Employee sends single messenge to other employee

    #Employee sends group messenge to other employee


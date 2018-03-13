from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException

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

    def test_layout_and_styling(self):
        #User visits home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        #User sees both the navbar and a body element
        self.browser.find_element_by_tag_name('nav')
        self.browser.find_element_by_tag_name('h1')

        #User visits 

        #User visits 


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


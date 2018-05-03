import time
# import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.keys import Keys
from unittest import skip

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

    def test_layout_and_styling_home(self):
        # User visits home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # User sees the page load
        assert 'DAWLAB Software' in self.browser.title

        # User sees the nav, h1, and footer elements
        self.browser.find_element_by_tag_name('nav')
        self.browser.find_element_by_tag_name('h1')
        self.browser.find_element_by_tag_name('footer')

        # User sees the correct bootswatch theme served from the bootswatch cdn
        navbar_background_color = self.browser.find_element_by_tag_name('nav')\
            .value_of_css_property("background-color")
        self.assertEqual(navbar_background_color, 'rgba(0, 0, 0, 0)')

        # CURRENTLY BROKEN User sees the correct static images
        # img_from_page = self.browser.find_element_by_tag_name('img')\
        #   .get_attribute('size')
        # img_from_file = os.path.join(os.path.dirname(__file__),
        #   '../content/static/img/Ali.jpg')
        # self.assertEqual(img_from_page, img_from_file)

        # HOST NAME

        # User sees the header in Arial or Times font
        h1_font_from_page = self.browser.find_element_by_tag_name('h1')\
            .value_of_css_property("font-family")
        self.assertEqual(h1_font_from_page, '"Arial", Times, serif')

    def test_layout_and_styling_our_team(self):
        our_team_page_url = '/content/'
        # User visits home page.
        combined_url = self.live_server_url + our_team_page_url
        self.browser.get(combined_url)
        self.browser.set_window_size(1024, 768)

        # User sees home page title
        assert 'DAWLAB Software' in self.browser.title

        # User sees the nav, h1, and footer elements
        self.browser.find_element_by_tag_name('nav')
        self.browser.find_element_by_tag_name('h1')

        # User sees the correct bootstrap theme
        navbar_background_color = self.browser.find_element_by_tag_name('nav')\
            .value_of_css_property("background-color")
        self.assertEqual(navbar_background_color, 'rgba(0, 0, 0, 0)')

        # CURRENTLY BROKEN
        # User sees the correct static images
        # img_from_page = self.browser.find_element_by_tag_name('img')\
        #   .get_attribute('size')
        # img_from_file = os.path.join(os.path.dirname(__file__),
        #   '../content/static/img/Ali.jpg')
        # self.assertEqual(img_from_page, img_from_file)

        # User sees the header in Arial or Times font
        h1_font_from_page = self.browser.find_element_by_tag_name('h1')\
            .value_of_css_property("font-family")
        self.assertEqual(h1_font_from_page, '"Arial", Times, serif')


class NavigationTest(FunctionalTest):

    def test_navigation_between_home_and_our_team(self):

        # User visits the home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        home_url = self.browser.current_url
        our_team_url = "/content/"
        employee_zone = "/authentication/"

        # User clicks the navbar company logo, remains on home page.
        self.browser.find_element_by_class_name('navbar-brand').click()
        self.wait_for(lambda: self.assertEqual(home_url,
                                               self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title

        # User clicks the navbar our_team option, is sent to our_team page.
        self.browser.find_element_by_link_text('Our Team').click()
        self.wait_for(lambda: self.assertIn(our_team_url,
                                            self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title

        # User clicks the navbar our_team option, stays on our_team page.
        self.browser.find_element_by_link_text('Our Team').click()
        self.wait_for(lambda: self.assertIn(our_team_url,
                                            self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title

        # User clicks the navbar company logo, is sent to home page.
        self.browser.find_element_by_class_name('navbar-brand').click()
        self.wait_for(lambda: self.assertEqual(home_url,
                                               self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title

        # User clicks the navbar employee_zone option, is sent to login page.
        self.browser.find_element_by_link_text('Employee Zone').click()
        self.wait_for(lambda: self.assertIn(employee_zone,
                                            self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title

        # User clicks the navbar our_team option, is sent to our_team page.
        self.browser.find_element_by_link_text('Our Team').click()
        self.wait_for(lambda: self.assertIn(our_team_url,
                                            self.browser.current_url))
        assert 'DAWLAB Software' in self.browser.title


class DataDisplayTest(FunctionalTest):

    @skip("Test broken, won't load query assets.")
    def test_data_display_our_team(self):

        our_team_page_url = '/content/'

        # User visits home page.
        combined_url = self.live_server_url + our_team_page_url
        self.browser.get(combined_url)
        self.browser.set_window_size(1024, 768)
        time.sleep(5)

        # User sees none of the card images are empty
        card_images = self.browser\
            .find_elements_by_class_name('profile-pictures')
        for i in card_images:
            self.assertNotEqual("", i.get_attribute("src"))

        # User sees none of the card headers are empty
        card_titles = self.browser.find_elements_by_class_name('card-title')
        for i in card_titles:
            self.assertNotEqual("", i.text)

        # User sees none of the card body texts are empty
        card_texts = self.browser.find_elements_by_class_name('card-text')
        for i in card_texts:
            self.assertNotEqual("", i.text)

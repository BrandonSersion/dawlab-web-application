from django.test import TestCase
from django.contrib.staticfiles import finders

class HomePageTest(TestCase):

    def test_home_page_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_static_exists(self): #not ideal, refactor to use self.client.get('/')
        assert finders.find('base.css')

class TeamPageTest(TestCase):

    def test_team_page_uses_home_template(self):
        response = self.client.get('/content/our_team/')
        self.assertTemplateUsed(response, 'our_team.html')

    def test_team_page_static_exists(self): #not ideal, refactor to use self.client.get('/')
        assert finders.find('base.css')


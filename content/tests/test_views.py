from django.test import TestCase
from django.contrib.staticfiles import finders

from content.models import Employee

class HomePageTest(TestCase):

    def test_home_page_uses_right_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_static_exists(self):  # not ideal, rewrite to use self.client.get('/')
        assert finders.find('base.css')

class TeamPageTest(TestCase):

    def test_team_page_uses_right_template(self):
        response = self.client.get('/content/')
        self.assertTemplateUsed(response, 'team.html')

    # missing static test


class EmployeeZoneTest(TestCase):

    def test_employee_zone_page_uses_right_template(self):
        response = self.client.get('/authentication/')
        self.assertTemplateUsed(response, 'account_login.html')

    # missing static test

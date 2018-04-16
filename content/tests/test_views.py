from django.test import TestCase
from django.contrib.staticfiles import finders

from content.models import Employee


class HomePageTest(TestCase):

    def test_home_page_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_static_exists(self):  # not ideal, refactor to use self.client.get('/')
        assert finders.find('base.css')

# class TeamPageTest(TestCase):

#     def test_team_page_uses_right_template_and_models(self, **kwargs):

        # response = self.client.get('/content/our_team/')
        # temp = Employee.objects.filter('first_name')
        # print(temp.first_name)

        # for i in Employee.objects.all():
        #     print("asf")
        # def unpack_employee_data(self, **kwargs):

        # response = self.client.get('/content/our_team/')
        # self.assertTemplateUsed(response, 'our_team.html', 
        #     {'last_name': last_name, 'first_name': first_name, 
        #     'job_title': job_title, 'job_description': job_description})

    # missing static test


class EmployeeZoneTest(TestCase):

    def test_employee_zone_page_uses_right_template(self):
        response = self.client.get('/content/employee_zone/')
        self.assertTemplateUsed(response, 'employee_zone.html')

    # missing static test

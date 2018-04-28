from django.test import TestCase
from content.models import Employee
from django.core.exceptions import ValidationError
from unittest import skip, expectedFailure


class EmployeeModelTest(TestCase):

    # EMPLOYEE DATABASE TESTS
    def test_employee_creation(self):
        test_employee = Employee()
        self.assertIsInstance(test_employee, Employee)

    def test_employee_save(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.full_clean()
        test_employee.save()
    
    def test_employee_data_inserts_correctly(self):
        test_string = "TEST_STRING"
        test_employee = Employee(last_name=test_string, first_name=test_string,
                        job_title=test_string, job_description=test_string, bio=test_string,
                        skills=test_string)
        test_employee.full_clean()
        test_employee.save()
        expected = test_string
        for attr,value in test_employee.__dict__.items():
            if attr == '_state' or attr == 'id':
                continue
            else:
                self.assertEqual(expected, value)

    # EMPLOYEE CONSTRAINT TESTS
    def test_no_empty_strings_in_employee_last_name(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.last_name = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_first_name(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.first_name = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_job_title(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.job_title = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_job_description(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.job_description = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_bio(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.bio = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_skills(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.skills = ''
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_last_name(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.last_name = 't'*21
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_first_name(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.first_name = 't'*21
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_job_title(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.job_title = 't'*21
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_job_description(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.job_description = 't'*1001
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_bio(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.bio = 't'*1001
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_skills(self):
        test_employee = Employee(last_name='test', first_name='test',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        test_employee.skills = 't'*1001
        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    # EMPLOYEE FUNCTION TESTS
    def test_str_representation(self):
        test_employee = Employee(last_name='LAST', first_name='FIRST',
                        job_title='test', job_description='test', bio='test',
                        skills='test')
        expected = test_employee.first_name + ' ' + test_employee.last_name
        self.assertEqual(expected, str(test_employee))
        
    # EMPLOYEE META TESTS
    def test_employee_duplicate_last_name_duplicate_first_name_fails(self):
        test_employee_1 = Employee(last_name='LAST', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()
        test_employee_2 = Employee(last_name='LAST', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_different_last_name_duplicate_first_name_passes(self):
        test_employee_1 = Employee(last_name='LAST', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()
        test_employee_2 = Employee(last_name='DIFFERENT', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_different_last_name_different_first_name_passes(self):
        test_employee_1 = Employee(last_name='LAST', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()
        test_employee_2 = Employee(last_name='DIFFERENT', first_name='DIFFERENT',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_duplicate_last_name_different_first_name_passes(self):
        test_employee_1 = Employee(last_name='LAST', first_name='FIRST',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()
        test_employee_2 = Employee(last_name='LAST', first_name='DIFFERENT',
                          job_title='test', job_description='test', bio='test',
                          skills='test')
        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    # def test_employee_ordering(self):

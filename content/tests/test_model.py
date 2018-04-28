from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest import skip, expectedFailure
from content.models import Employee

# Unit tests written using the Arrange-Act-Assert pattern


class EmployeeModelTest(TestCase):

    # EMPLOYEE DATABASE TESTS
    def test_can_create_employee(self):
        # arrange
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        # act
        test_employee.full_clean()
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        # assert
        self.assertIsInstance(test_employee_from_db, Employee)

    def test_employee_data_inserts_correctly(self):
        test_employee = Employee(
            last_name='test', first_name='test',
            job_title='test', job_description='test',
            bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        expected = 'test'

        test_employee_from_db = Employee.objects.get(pk=1)

        for attr, value in test_employee_from_db.__dict__.items():
            if attr == '_state' or attr == 'id':  # Exclude auto generated attributes
                continue
            else:
                self.assertEqual(expected, value)

    def test_employee_last_name_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.last_name = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.last_name)

    def test_employee_first_name_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.first_name = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.first_name)

    def test_employee_job_title_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.job_title = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.job_title)

    def test_employee_job_description_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.job_description = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.job_description)

    def test_employee_bio_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.bio = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.bio)

    def test_employee_skills_can_be_overwritten(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee.full_clean()
        test_employee.save()
        changed_string = "CHANGED"
        expected = changed_string

        test_employee.skills = changed_string
        test_employee.full_clean
        test_employee.save()
        test_employee_from_db = Employee.objects.get(pk=1)

        self.assertEqual(expected, test_employee_from_db.skills)

    def test_multiple_employees_can_be_created(self):
        test_employee_1 = Employee(
            last_name='name1', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_1.full_clean
        test_employee_1.save()
        test_employee_2 = Employee(
            last_name='name2', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_2.full_clean
        test_employee_2.save()
        test_employee_3 = Employee(
            last_name='name3', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_3.full_clean
        test_employee_3.save()

        test_employee_1_from_db = Employee.objects.get(pk=1)
        test_employee_2_from_db = Employee.objects.get(pk=2)
        test_employee_3_from_db = Employee.objects.get(pk=3)

        self.assertIsInstance(test_employee_1_from_db, Employee)
        self.assertIsInstance(test_employee_2_from_db, Employee)
        self.assertIsInstance(test_employee_3_from_db, Employee)

    # EMPLOYEE CONSTRAINT TESTS
    def test_no_empty_strings_in_employee_last_name(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.last_name = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_first_name(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.first_name = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_job_title(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.job_title = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_job_description(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.job_description = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_bio(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.bio = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    def test_no_empty_strings_in_employee_skills(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.skills = ''

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_last_name(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.last_name = 't'*21

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_first_name(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.first_name = 't'*21

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_job_title(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.job_title = 't'*21

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_job_description(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.job_description = 't'*1001

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_bio(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.bio = 't'*1001

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    @skip("""Test fails. SqlLite does not enforce character constraints.
             Switch to PostgreSQL and try again.""")
    def test_max_length_on_employee_skills(self):
        test_employee = Employee(
            last_name='test', first_name='test', job_title='test',
            job_description='test', bio='test', skills='test')

        test_employee.skills = 't'*1001

        with self.assertRaises(ValidationError):
            test_employee.full_clean()
            test_employee.save()

    # EMPLOYEE FUNCTION TESTS
    def test_str_representation(self):
        test_employee = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')

        expected = test_employee.first_name + ' ' + test_employee.last_name

        self.assertEqual(expected, str(test_employee))

    # EMPLOYEE META TESTS
    def test_employee_duplicate_last_name_duplicate_first_name_fails(self):
        test_employee_1 = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()

        test_employee_2 = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')

        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_different_last_name_duplicate_first_name_passes(self):
        test_employee_1 = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()

        test_employee_2 = Employee(
            last_name='DIFFERENT', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')

        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_different_last_name_different_first_name_passes(self):
        test_employee_1 = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()

        test_employee_2 = Employee(
            last_name='DIFFERENT', first_name='DIFFERENT', job_title='test',
            job_description='test', bio='test', skills='test')

        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    @expectedFailure
    def test_employee_duplicate_last_name_different_first_name_passes(self):
        test_employee_1 = Employee(
            last_name='LAST', first_name='FIRST', job_title='test',
            job_description='test', bio='test', skills='test')
        test_employee_1.full_clean()
        test_employee_1.save()

        test_employee_2 = Employee(
            last_name='LAST', first_name='DIFFERENT', job_title='test',
            job_description='test', bio='test', skills='test')

        with self.assertRaises(ValidationError):
            test_employee_2.full_clean()
            test_employee_2.save()

    # test ordering

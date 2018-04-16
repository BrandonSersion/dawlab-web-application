from django.test import TestCase
from content.models import Employee
from django.core.exceptions import ValidationError
from unittest import skip


class EmployeeModelTest(TestCase):

    # HELPER FUNCTIONS

    def full_save(self, instance):
        instance.full_clean()
        instance.save()

    # Test constants used for the Employee class.
    def create_test_constants(self):

        def create_test_constants(self):
            FIRST_NAME = 'Charles' 
            LAST_NAME = 'Bronson'
            JOB_TITLE = 'Agent'
            JOB_DESCRIPTION = 'Tough Guy'
            SKILLS = 'Fighting Crime'
            BIO = ('He starred in films such as Once Upon a Time in the West, The Magnificent Seven, The Dirty Dozen,'
            ' The Great Escape, Battle of the Bulge, Rider on the Rain, The Mechanic, and the Death Wish series.'
            ' He was often cast in the role of a police officer, gunfighter, or vigilante in a revenge-oriented plot.')

        def create_test_db_entry(self):
            EMPLOYEE = Employee(
                    first_name=FIRST_NAME,
                    last_name=LAST_NAME,
                    job_title=JOB_TITLE,
                    job_description=JOB_DESCRIPTION,
                    skills=SKILLS,
                    bio=BIO
            )
            full_save(EMPLOYEE)

        create_test_constants()
        create_test_db_entry()

    # TESTS
    def test_data_inserts_correctly(self):
        create_test_constants()

        expected = FIRST_NAME
        self.assertEqual(expected, EMPLOYEE.first_name)

        expected = LAST_NAME
        self.assertEqual(expected, EMPLOYEE.last_name)

        expected = JOB_TITLE
        self.assertEqual(expected, EMPLOYEE.job_title)

        expected = JOB_DESCRIPTION
        self.assertEqual(expected, EMPLOYEE.job_description)

        expected = SKILLS
        self.assertEqual(expected, EMPLOYEE.skills)

        expected = BIO
        self.assertEqual(expected, EMPLOYEE.bio)

    def test_default_employee_string_is_null(self):
        empty_employee = Employee()
        full_save(empty_employee)

        expected = ''
        self.assertEqual(expected, empty_employee.first_name)
        self.assertEqual(expected, empty_employee.last_name)
        self.assertEqual(expected, empty_employee.job_title)
        self.assertEqual(expected, empty_employee.job_description)
        self.assertEqual(expected, empty_employee.bio)
        self.assertEqual(expected, empty_employee.skills)

    def test_employee_lookup_prints_first_name_last_name(self):
        create_test_constants()

        expected = "Charles Bronson"
        self.assertEqual(expected, EMPLOYEE.__str__())

    def test_duplicate_employee_name_is_invalid(self):
        create_test_constants()

        expected = Employee(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            job_title='These',
            job_description='strings',
            skills='can',
            bio='differ.'
        )

        with self.assertRaises(ValidationError):
            full_save(expected)

    def test_duplicate_first_name_different_last_name_is_valid(self):
        duplicate_first_name = FIRST_NAME

        employee_1 = Employee(
            first_name=duplicate_first_name,
            last_name=LAST_NAME,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )
        full_save(employee_1)
        employee_2 = Employee(
            first_name=duplicate_first_name,
            last_name='Different_last_name',
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )
        full_save(employee_2)

    def test_duplicate_last_name_different_first_name_is_valid(self):
        duplicate_last_name = LAST_NAME

        employee_1 = Employee(
            first_name=FIRST_NAME,
            last_name=duplicate_last_name,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )
        full_save(employee_1)
        employee_2 = Employee(
            first_name='Different_first_name',
            last_name=duplicate_last_name,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )
        full_save(employee_2)


class CharacterLimitTest(EmployeeModelTest):
    # Tests show sqllite is not enforcing character constraints.
    # Switch to postgres, then test again.

    @skip('')
    def test_character_limits_on_first_name(self):       
        employee = Employee(
            first_name='This string is too long.',
            last_name=LAST_NAME,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_last_name(self):
        employee = Employee(
            first_name=FIRST_NAME
            last_name='This string is too long.',
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_job_title(self):
        employee = Employee(
            first_name=FIRST_NAME
            last_name=LAST_NAME,
            job_title='This string is too long.',
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_job_description(self):
        employee = Employee(
            first_name=FIRST_NAME
            last_name=LAST_NAME,
            job_title=JOB_TITLE,
            job_description=('This string is too long. This string is too long. This string is too long. This'
            ' string is too long. This string is too long. This string is too long. This string is too long. This' 
            ' string is too long. This string is too long. This string is too long. This string is too long.'),
            skills=SKILLS,
            bio=BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_skills(self):
        employee = Employee(
            first_name=FIRST_NAME
            last_name=LAST_NAME,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=('This string is too long. This string is too long. This string is too long. This string is'
            ' too long. This string is too long. This string is too long. This string is too long. This string is'
            ' too long. This string is too long. This string is too long. This string is too long.'),
            bio=BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_bio(self):
        employee = Employee(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            job_title=JOB_TITLE,
            job_description=JOB_DESCRIPTION,
            skills=SKILLS,
            bio=('This string is too long. This string is too long. This string is too long. This string is too'
            ' long. This string is too long. This string is too long. This string is too long. This string is too'
            ' long. This string is too long. This string is too long. This string is too long.')
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

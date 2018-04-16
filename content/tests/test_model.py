from django.test import TestCase
from content.models import Employee
from django.core.exceptions import ValidationError
from unittest import skip

class EmployeeModelTest(TestCase):

    # Global test constants used for the Employee class.
    FIRST_NAME = 'Charles'
    LAST_NAME = 'Bronson'
    JOB_TITLE = 'Agent'
    JOB DESCRIPTION = 'Tough Guy'
    SKILLS = 'Fighting Crime'
    BIO = ('He starred in films such as Once Upon a Time in the West, The Magnificent Seven, The Dirty Dozen,'
    ' The Great Escape, Battle of the Bulge, Rider on the Rain, The Mechanic, and the Death Wish series.'
    ' He was often cast in the role of a police officer, gunfighter, or vigilante in a revenge-oriented plot.')
    EMPLOYEE = Employee(
            first_name = FIRST_NAME,
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS, 
            bio = BIO
    )

    def test_default_text_is_null(self):
        self.assertEqual(EMPLOYEE.last_name, '')
        self.assertEqual(EMPLOYEE.first_name, '')
        self.assertEqual(EMPLOYEE.job_title, '')
        self.assertEqual(EMPLOYEE.job_description, '')
        self.assertEqual(EMPLOYEE.bio, '')
        self.assertEqual(EMPLOYEE.skills, '')

    def test_can_insert_data(self):
        EMPLOYEE.full_clean()
        EMPLOYEE.save()

        self.assertEqual(EMPLOYEE.first_name, FIRST_NAME)
        self.assertEqual(EMPLOYEE.last_name, LAST_NAME)
        self.assertEqual(EMPLOYEE.job_title, JOB_TITLE)
        self.assertEqual(EMPLOYEE.job_description, JOB_DESCRIPTION)
        self.assertEqual(EMPLOYEE.skills, SKILLS)
        self.assertEqual(EMPLOYEE.bio, BIO)

    def test_employee_lookup_prints_first_name_last_name(self):
        employee = Employee(
            first_name = FIRST_NAME, 
            last_name = LAST_NAME, 
            job_title =  JOB_TITLE, 
            job_description = JOB DESCRIPTION, 
            skills = SKILLS, 
            bio = BIO,
        )
        employee.full_clean()
        employee.save()
        results = employee.__str__()

        expected = "Charles Bronson"
        self.assertEqual(results, expected)
        
    def test_duplicate_employee_name_is_invalid(self):
        employee_1 = Employee(
            first_name = FIRST_NAME,
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS, 
            bio = BIO
        )
        employee_1.full_clean()
        employee_1.save()
        employee_2 = Employee(
            first_name = FIRST_NAME,
            last_name = LAST_NAME,
            job_title = 'These',
            job_description = 'strings',
            skills = 'can',
            bio = 'differ.'
        )

        with self.assertRaises(ValidationError):
            employee_2.full_clean()
            employee_2.save()

    def test_duplicate_first_name_different_last_name_is_valid(self):
        duplicate_first_name = FIRST_NAME 

        employee_1 = Employee(
            first_name = duplicate_first_name,
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )
        employee_1.full_clean()
        employee_1.save()
        employee_2 = Employee(
            first_name = duplicate_first_name,
            last_name = 'Different_last_name',
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )
        employee_2.full_clean()
        employee_2.save()

    def test_duplicate_last_name_different_first_name_is_valid(self):
        duplicate_last_name = LAST_NAME

        employee_1 = Employee(
            first_name = FIRST_NAME,
            last_name = duplicate_last_name,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )
        employee_1.full_clean()
        employee_1.save()
        employee_2 = Employee(
            first_name = 'Different_first_name',
            last_name = duplicate_last_name,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )
        employee_2.full_clean()
        employee_2.save()
    

    
class CharacterLimitTest(EmployeeModelTest):
     #Tests show sqllite is not enforcing character constraints. Switch to postgres, then test again.

    @skip('')
    def test_character_limits_on_first_name(self):       
        employee = Employee(
            first_name = 'This string is too long.',
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_last_name(self):
        employee = Employee(
            first_name = FIRST_NAME
            last_name = 'This string is too long.',
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_job_title(self):
        employee = Employee(
            first_name = FIRST_NAME
            last_name = LAST_NAME,
            job_title = 'This string is too long.',
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_job_description(self):
        employee = Employee(
            first_name = FIRST_NAME
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = ('This string is too long. This string is too long. This string is too long. This'
            ' string is too long. This string is too long. This string is too long. This string is too long. This' 
            ' string is too long. This string is too long. This string is too long. This string is too long.'),
            skills = SKILLS,
            bio = BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_skills(self):
        employee = Employee(
            first_name = FIRST_NAME
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = ('This string is too long. This string is too long. This string is too long. This string is'
            ' too long. This string is too long. This string is too long. This string is too long. This string is'
            ' too long. This string is too long. This string is too long. This string is too long.'),
            bio = BIO
        )

        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()

    @skip('')
    def test_character_limits_on_bio(self):
        employee = Employee(
            first_name = FIRST_NAME,
            last_name = LAST_NAME,
            job_title = JOB_TITLE,
            job_description = JOB_DESCRIPTION,
            skills = SKILLS,
            bio = ('This string is too long. This string is too long. This string is too long. This string is too'
            ' long. This string is too long. This string is too long. This string is too long. This string is too'
            ' long. This string is too long. This string is too long. This string is too long.')
        )
            
        with self.assertRaises(ValidationError):
            employee.full_clean()
            employee.save()


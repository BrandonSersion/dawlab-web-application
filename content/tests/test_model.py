from django.test import TestCase
from content.models import Employee
from django.core.exceptions import ValidationError
from unittest import skip

class EmployeeModelTest(TestCase):

    def test_default_text(self):
        employee = Employee()
        self.assertEqual(employee.last_name, '')
        self.assertEqual(employee.first_name, '')
        self.assertEqual(employee.job_title, '')
        self.assertEqual(employee.job_description, '')
        self.assertEqual(employee.bio, '')
        self.assertEqual(employee.skills, '')

    def test_employee_lookup_default_first_name_last_name(self):
        employee = Employee(first_name = 'Charles', last_name = 'Bronson', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee.full_clean()
        
        employee.save()
        self.assertEqual(employee.__str__(), 'Charles Bronson')

    def test_can_insert_data(self):
        employee = Employee(first_name = 'Paul', last_name = 'Blart', job_title = 'Mall Cop', job_description = 'The hero of the story.', skills='Fighting crime.', bio='Paul Blart: Mall Cop is a 2009 American action comedy film co-written by Kevin James, who stars as the title character, Paul Blart. Filming began in February 2008 with most of the shooting taking place at the Burlington Mall in Burlington, Massachusetts.')
        self.assertEqual(employee.first_name, 'Paul')
        self.assertEqual(employee.last_name, 'Blart')
        self.assertEqual(employee.job_title, 'Mall Cop')
        self.assertEqual(employee.job_description, 'The hero of the story.')
        self.assertEqual(employee.skills, 'Fighting crime.')
        self.assertEqual(employee.bio, 'Paul Blart: Mall Cop is a 2009 American action comedy film co-written by Kevin James, who stars as the title character, Paul Blart. Filming began in February 2008 with most of the shooting taking place at the Burlington Mall in Burlington, Massachusetts.')
        
        employee.full_clean()
        employee.save()

    def test_duplicate_employee_names_are_invalid(self):
        employee_1 = Employee(first_name = 'Charles', last_name = 'Bronson', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_2 = Employee(first_name = 'Charles', last_name = 'Bronson', job_title = 'This', job_description = 'text', skills='differs', bio='.')
        employee_1.full_clean()
        employee_1.save()

        with self.assertRaises(ValidationError):
            employee_2.full_clean()

    def test_similar_employee_names_are_valid(self):
        employee_1 = Employee(first_name = 'Charles', last_name = 'Bronson', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_2 = Employee(first_name = 'Charles', last_name = 'Pastor', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_3 = Employee(first_name = 'Eddy', last_name = 'Bronson', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        
        employee_1.full_clean()
        employee_1.save()
        employee_2.full_clean()
        employee_3.full_clean()
    

    #Sqllite is not enforcing character constraints. Switch to postgres, then test.
    @skip('')
    def test_character_limits(self):       
        employee_1 = Employee(first_name = '123456789012345678901', last_name = 'Phal', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_2 = Employee(first_name = 'Aeqs', last_name = '123456789012345678901', job_title = 'Agent', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_3 = Employee(first_name = 'New', last_name = 'Hat', job_title = '123456789012345678901', job_description = 'Tough guy.', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_4 = Employee(first_name = 'Noom', last_name = 'Ewws', job_title = 'Agent', job_description = '0123456789012345678901234567890123456789012345678901234567890', skills='Fighting crime.', bio='Steven Frederic Seagal (/sɪˈɡɑːl/; born April 10, 1952) is an American actor, producer, screenwriter, director, martial artist, and musician who holds American, Russian, and Serbian citizenship.')
        employee_5 = Employee(first_name = 'FASew', last_name = 'Auat', job_title = 'Agent', job_description = 'Cart', skills='0123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890.', bio='reasonsa')
        employee_6 = Employee(first_name = 'Hamo', last_name = 'Looe', job_title = 'Agent', job_description = 'Cart', skills='Fighting crime.', bio='0123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890012345678901234567890123456789012345678901234567890123456789001234567890123456789012345678901234567890123456789012345678900123456789012345678901234567890123456789012345678901234567890')

        with self.assertRaises(ValidationError):
            employee_1.full_clean()
            employee_1.save()

            employee_2.full_clean()

            employee_3.full_clean()

            employee_4.full_clean()



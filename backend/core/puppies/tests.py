from django.test import TestCase
from .models import Puppy


class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        """
        data setup for the testing of the class.
        """
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_string_representation(self):
        """
        Test the name of a puppy is returned instead of the default 'Puppy object'
        """
        puppy = Puppy(name="Rocky")
        self.assertEqual(str(puppy), puppy.name)

    def test_correct_pluralization_of_Puppy(self):
        """ Test the correct plural word of Puppy => Puppies not Puppys """
        self.assertEqual(str(Puppy._meta.verbose_name_plural), 'puppies')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")

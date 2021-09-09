from random import randrange

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Puppy


class GetAllPuppiesTest(TestCase):
    """ Test module for GET all puppies API """
    client = Client()
    list_endpoint = '/api/v1/puppies/'
    detail_endpoint = '/api/v1/puppy/'
    id = 1

    def setUp(self):
        """
        Data preparation to be used in tests i.e. creating objects of Puppy Model for testing purposes.
        """
        Puppy.objects.create(name='The Rock', age=3, breed='Bull Dog', color='Black')

        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')

        Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')

        Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')

    def get_random_id(self):
        """
        Generate an integer value between two and the number of Puppy model object plus 1.
        :return: an integer between 'id+1' and 'Puppy.objects.all().count())'
        """
        stop = Puppy.objects.all().count()
        return randrange(self.id + 1, stop, 1)

    def test_puppies_listview(self):
        """
        a test for getting all puppies without pagination using path/url.
        :return: Assertion Result.
        """
        self.get_random_id()

        response = self.client.get(path=self.list_endpoint, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, Puppy.objects.get(id=self.id).name)

        self.assertContains(response, Puppy.objects.get(id=self.get_random_id()).name)

    def test_puppies_listview_name(self):
        """
        a test for getting all puppies without pagination, using the view 'name'.
        :return: Assertion Result.
        """
        response = self.client.get(reverse('puppies_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, Puppy.objects.get(id=self.id).name)

        self.assertContains(response, Puppy.objects.get(id=self.get_random_id()).name)

    def test_puppies_detail_view(self):
        """
        Test the api can get an single puppy (detail page).
        :return: Assertion Result.
        """

        puppy = Puppy.objects.get(id=self.id)

        url = '{}{}/'.format(self.detail_endpoint, puppy.pk)

        response = self.client.get(path=url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, puppy.name)

        self.assertContains(response, puppy.color)

        self.assertContains(response, puppy.age)

        self.assertContains(response, puppy.breed)

        self.assertNotContains(response, Puppy.objects.get(id=self.get_random_id()).name)

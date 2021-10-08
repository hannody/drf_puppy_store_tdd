from random import randrange

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Puppy


class PuppiesViewsTest(TestCase):
    """ Test module for all (GET, POST, UPDATE and DELETE) puppies API """
    client = APIClient()
    list_endpoint = '/api/v1/puppies/'
    detail_endpoint = '/api/v1/puppy/'
    post_endpoint = '/api/v1/puppy/new/'
    delete_endpoint = '/api/v1/puppy/delete/'
    update_endpoint = '/api/v1/puppy/update/'
    ID = 1

    def setUp(self):
        """
        Data preparation to be used in tests i.e. creating objects of Puppy Model for testing purposes.
        """
        Puppy.objects.create(name='The Rock', age=3, breed='Bull Dog', color='Black')

        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')

        Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')

        Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')

        User = get_user_model()

        self.user = User.objects.create_user(email='normal@user.com', password='foo')

    def get_random_id(self):
        """
        Generate an integer value between number "2" and the count of (objects count) of Puppy model object plus 1.
        :return: an integer between 'id+1' and 'Puppy.objects.all().count()) + 1'
        """
        stop = Puppy.objects.all().count()
        random_id = randrange(start=self.ID, stop=stop, step=1)
        return self.ID + random_id

    def test_get_random_number(self):
        stop = Puppy.objects.all().count()
        random_id = randrange(self.ID, stop, 1)
        self.assertTrue(random_id <= stop)

    def test_puppies_listview(self):
        """
        a test for getting all puppies without pagination using path/url.
        :return: Assertion
        """
        self.get_random_id()

        # Unauthenticated user action.
        response = self.client.get(path=self.list_endpoint)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.get(path=self.list_endpoint)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, Puppy.objects.get(id=self.ID).name)

        self.assertContains(response, Puppy.objects.get(id=self.get_random_id()).name)

    def test_puppies_listview_name(self):
        """
        a test for getting all puppies without pagination, using the view 'name'.
        :return: Assertion
        """

        # Unauthenticated user action.
        response = self.client.get(reverse('puppies_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.get(reverse('puppies_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, Puppy.objects.get(id=self.ID).name)

        self.assertContains(response, Puppy.objects.get(id=self.get_random_id()).name)

    def test_puppies_detail_view(self):
        """
        Test the api can get a single puppy (detail page).
        :return: Assertion
        """

        puppy = Puppy.objects.get(id=self.ID)
        url = '{}{}/'.format(self.detail_endpoint, puppy.pk)

        # Unauthenticated user action.
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, puppy.name)
        self.assertContains(response, puppy.color)
        self.assertContains(response, puppy.age)
        self.assertContains(response, puppy.breed)
        self.assertNotContains(response, Puppy.objects.get(id=self.get_random_id()).name)

    def test_create_new_puppy(self):
        """
        Creating a new puppy object Create_RUD
        :return: Assertion
        """
        new_puppy = {
            'name': 'Cyborg',
            'age': 2,
            'breed': 'German Shepherd',
            'color': 'Black and Orange'
        }
        previous_object_count = Puppy.objects.all().count()

        # Unauthenticated user action.
        response = self.client.post(path=self.post_endpoint, data=new_puppy, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.post(path=self.post_endpoint, data=new_puppy, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Puppy.objects.count() > previous_object_count)

    def test_delete_puppy(self):
        """
        Deleting puppy object CRU_Delete
        :return: Assertion
        """
        puppy = Puppy.objects.get(id=self.ID)
        previous_object_count = Puppy.objects.all().count()
        url = '{}{}/'.format(self.delete_endpoint, puppy.pk)

        # Unauthenticated user action.
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(Puppy.objects.count() < previous_object_count)

    def test_full_update_puppy_detail(self):
        """
        Test for update full puppy details using PUT method.
        :return: Assertion
        """
        update_id = self.get_random_id()
        puppy = Puppy.objects.get(id=update_id)
        old_name = puppy.name
        old_updated_at = puppy.updated_at
        updated_puppy_data = {"name": "Weasel", "age": 1, "breed": "Sloughi", "color": puppy.color}

        # Unauthenticated user action.
        url = '{}{}/'.format(self.update_endpoint, puppy.pk)
        response = self.client.put(path=url, data=updated_puppy_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.put(path=url, data=updated_puppy_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotContains(response, old_name)
        self.assertContains(response, puppy.color)
        self.assertNotContains(response, old_updated_at)

    def test_partial_update_patch_puppy(self):
        """
        Test for partial update using PATCH.
        :return: Assertion
        """
        update_id = self.get_random_id()
        puppy = Puppy.objects.get(id=update_id)
        old_name = puppy.name
        old_updated_at = puppy.updated_at
        new_name = "Yalong"
        patch_puppy_data = {"name": new_name}
        url = '{}{}/'.format(self.update_endpoint, puppy.pk)

        # Unauthenticated user action.
        response = self.client.patch(path=url, data=patch_puppy_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(email='normal@user.com', password='foo')
        response = self.client.patch(path=url, data=patch_puppy_data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotContains(response, old_name)
        self.assertContains(response, new_name)
        self.assertContains(response, puppy.color)
        self.assertContains(response, puppy.age)
        self.assertContains(response, puppy.breed)
        self.assertNotContains(response, old_updated_at)

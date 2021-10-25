from django.test import SimpleTestCase
from rest_framework import status

from core.urls import ADMIN_URL


class TestAdminCustomURL(SimpleTestCase):
    """
    Tests for Admin page reachability.
    """

    def setUp(self) -> None:
        """
        Init data for other tests.
        """
        self.custom_admin_url = '/{}{}/'.format(ADMIN_URL, 'login')
        self.default_admin_ulr = '/{}/{}/'.format('admin', 'login')

    def test_new_url(self):
        """
        Test for new admin url.
        """
        response = self.client.get(self.custom_admin_url)
        self.assertEqual(response.status_code, 200)
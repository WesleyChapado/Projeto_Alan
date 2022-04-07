from rest_framework import status
from rest_framework.test import APITestCase

class EndpointsTests(APITestCase):
    def test_get_user(self):
        url = '/v1.0/register/user/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization(self):
        url = '/v1.0/register/organization/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user(self):
        url = '/v1.0/register/user/'
        data ={
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_organization(self):
        url = '/v1.0/register/organization/'
        data ={
            "name": "OrganizationTest",
            "status": "false",
            "created": "2022-04-03T17:24:00-03:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

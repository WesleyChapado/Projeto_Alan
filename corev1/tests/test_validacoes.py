from rest_framework import status
from rest_framework.test import APITestCase

class ValidacoesTests(APITestCase):
    def test_create_user_with_invalid_password(self):
        url = '/v1.0/register/user/'
        data ={
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            # a senha deve conter no mínimo 6 caracteres, uma letra maiúscula e uma letra minúscula
            "password": "1234a",
            "organization": "UT"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_same_email(self):
        # primeiro usuário
        url = '/v1.0/register/user/'
        data ={
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT"
        }
        self.client.post(url, data, format='json')

        # segundo usuário
        url = '/v1.0/register/user/'
        data ={
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            # não pode usar um email já cadastrado
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_org_with_invalid_name(self):
        url = '/v1.0/register/organization/'
        data ={
            # o nome da organização não pode ser maior do que 30 caracteres
            "name": "OrganizationTest_OrganizationTest",
            "status": "false",
            "created": "2022-04-03T17:24:00-03:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

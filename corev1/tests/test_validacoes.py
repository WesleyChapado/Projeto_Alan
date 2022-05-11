from rest_framework import status
from rest_framework.test import APITestCase

class ValidacoesTests(APITestCase):
    def test_create_user_with_invalid_password(self):
        '''
            Cria um usuário não atendendo os critérios de senha,
            os critérios são: 
                conter no mínimo 6 caracteres, 
                conter uma letra maiúscula, 
                conter uma letra minúscula
        '''
        url = '/v1.0/register/user/create/'
        data ={
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234a",
            "organization": "UT",
            "plan_id": ""
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_same_email(self):
        '''
            Tenta fazer a criação de dois usuários com o mesmo email,
            isso não é permitido pois usamos o email para validações
        '''
        url = '/v1.0/register/user/create/'
        data ={
            "username": "UsernameTest1",
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT",
            "plan_id": ""
        }
        self.client.post(url, data, format='json')

        url = '/v1.0/register/user/create/'
        data ={
            "username": "UsernameTest2",
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT",
            "plan_id": ""
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



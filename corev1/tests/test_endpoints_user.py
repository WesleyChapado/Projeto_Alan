from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserModel
from rest_framework.authtoken.models import Token

class UserEndpointsTests(APITestCase):
    def setUp(self):
        '''
            Cria o usuário para ser usado nos próximos testes
        '''
        self.user = UserModel.objects.create(
            username= "testUsername",
            first_name= "testFN",
            last_name= "testLN",
            email= "test1@gmai.com",
            password= "1234aB",
            organization= "testOrganization1",
        )
        self.token_user = Token.objects.get_or_create(user=self.user)

    def test_post_create_user_sem_campo_plan_id(self):
        '''
            Cria um novo usuário, caso o campo plan_id não seja informado 
            um plano com os valores padrões será criado, os valores são:
                plan_type = free, 
                max_knowledge_base = 1, 
                max_megabyte = 5, 
                max_users = 1
        '''
        url = '/v1.0/register/user/create/'
        data ={
            "username": "UsernameTest",
            "first_name": "UserTestFN",
            "last_name": "UserTestLN",
            "email": "UserTest@gmail.com",
            "password": "1234aB",
            "organization": "UT",
            "plan_id": ""
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lista_usuarios(self):
        '''
            Lista todos os usuários, um token deve ser informado no HEADER
        '''
        url = '/v1.0/register/user/list/'
        response = self.client.get(
            url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserModel
from rest_framework.authtoken.models import Token

class EndpointsTests(APITestCase):
    def setUp(self):
        '''
            Cria dois usuários para serem usados nos próximos testes
        '''
        self.user1 = UserModel.objects.create(
            username= "testUsername1",
            first_name= "testFN1",
            last_name= "testLN1",
            email= "test1@gmail.com",
            password= "1234aB",
            organization= "testOrganization1",
        )
        self.user2 = UserModel.objects.create(
            username= "testUsername2",
            first_name= "testFN2",
            last_name= "testLN2",
            email= "test2@gmail.com",
            password= "1234aB",
            organization= "testOrganization2",
        )
        self.token_user1 = Token.objects.get_or_create(user=self.user1)
        self.token_user2 = Token.objects.get_or_create(user=self.user2)

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
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lista_organization(self):
        '''
            Lista todas as organizações, um token deve ser informado no HEADER
        '''
        url = '/v1.0/register/organization/'
        response = self.client.get(
            url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_lista_plans(self):
        '''
            Lista todos os planos, um token deve ser informado no HEADER
        '''
        url = '/v1.0/register/plan/'
        response = self.client.get(
            url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_folder(self):
        '''
            Cria uma pasta para o usuário 1
        '''
        url = '/v1.0/register/folder/'
        data ={
            "name" : "testFolderName"
        }
        response = self.client.post(
            url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_unnamed_folder(self):
        '''
            Tenta criar uma pasta sem nome, isso não é permitido
        '''
        url = '/v1.0/register/folder/'
        data ={
            "name" : ""
        }
        response = self.client.post(
            url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list_all_token_owner_folders(self):
        '''
            Lista todas as pastas do proprietátio do token
        '''
        url = '/v1.0/register/folder/'
        response = self.client.get(
            url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if self.user2.email not in response.data.get('message', {}):
            raise AssertionError(f'Estas pastas não pertencem ao usuário {self.user2.email}')
    
    def test_try_to_delete_a_folder_of_another_user(self):
        '''
            Tenta apagar uma pasta de outro usuário, isso não é permitido
        '''
        url_post = '/v1.0/register/folder/'
        data ={
            "name" : "testFolderName"
        }
        response_post = self.client.post(
            url_post, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        data_delete = response_post.data.get('data', {})
        if data_delete:
            id_delete = data_delete['id']
            url_delete = f'/v1.0/register/folder/{id_delete}'
            response_delete = self.client.delete(
                url_delete,
                format='json',
                HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
            )
            self.assertEqual(response_delete.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise AssertionError('O teste não foi executado, devido a falha na criação da pasta')

    def test_try_to_change_a_folder_of_another_user(self):
        '''
            Tenta alterar uma pasta de outro usuário, isso não é permitido
        '''
        url_post = '/v1.0/register/folder/'
        data_post ={
            "name" : "testFolderName"
        }
        response_post = self.client.post(
            url_post, 
            data_post, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        data_put = response_post.data.get('data', {})
        if data_put:
            id_put = data_put['id']
            url_put = f'/v1.0/register/folder/{id_put}'
            data_put ={
            "name" : "testNewFolderName"
        }
            response_put = self.client.put(
                url_put,
                data_put,
                format='json',
                HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
            )
            self.assertEqual(response_put.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise AssertionError('O teste não foi executado, devido a falha na criação da pasta')
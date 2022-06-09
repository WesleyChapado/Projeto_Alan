from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserModel
from rest_framework.authtoken.models import Token

class DocumentEndpointsTests(APITestCase):
    def setUp(self):
        '''
            Cria a estrutura inicial para os testes
        '''
        # cria os usuários
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
        # cria tokens
        self.token_user1 = Token.objects.get_or_create(user=self.user1)
        self.token_user2 = Token.objects.get_or_create(user=self.user2)

        # url usada nos testes
        self.url = '/v1.0/register/document/'

        # inclui um documento no banco, o usuário 1 é o proprietário
        with open('corev1/tests/pdf_test.pdf', 'rb') as file:
            self.document = self.client.post(
                self.url,{
                    'name':'testNameDocument',
                    'file': file
                },
                HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
            )

    def test_post_create_document(self):
        '''
            Cria um documento para o usuário 2
        '''
        with open('corev1/tests/pdf_test.pdf', 'rb') as file:
            response = self.client.post(
                self.url,{
                    'name':'testNameDocument',
                    'file': file
                },
                HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)       

    def test_post_create_an_unnamed_document(self):
        '''
            Cria um documento sem nome para o usuário 2, isso não é permitido
        '''
        with open('corev1/tests/pdf_test.pdf', 'rb') as file:
            response = self.client.post(
                self.url,{
                    'name':'',
                    'file': file
                },
                HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_create_a_document_without_attaching_a_file(self):
        '''
            Cria um documento para o usuário 2, sem anexar um arquivo, isso não é permitido
        '''
        response = self.client.post(
            self.url,{
                'name':'testNameDocument'
            },
            HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list_all_token_owner_documents(self):
        '''
            Lista todos os documentos do proprietário do token
        '''
        response = self.client.get(
            self.url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if self.user1.email not in response.data.get('message', {}):
            raise AssertionError(f'Estas pastas não pertencem ao usuário {self.user1.email}')

    def test_try_to_delete_a_document_of_another_user(self):
        '''
            Tenta apagar um documento de outro usuário, isso não é permitido
        '''
        data_delete = self.document.data.get('data', {})
        if data_delete:
            uuid_delete = data_delete['uuid']
            url_delete = f'{self.url}{uuid_delete}'
            response = self.client.delete(
                url_delete,
                format='json',
                HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
            )
            self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise AssertionError('O teste não foi executado, devido a falha na criação do documento')
    
    def test_try_to_change_a_document_of_another_user(self):
        '''
            Tenta atualizar um documento de outro usuário, isso não é permitido
        '''
        data_put = self.document.data.get('data', {})
        if data_put:
            uuid_put = data_put['uuid']
            url_put = f'{self.url}{uuid_put}'
            with open('corev1/tests/pdf_test.pdf', 'rb') as file:
                response = self.client.put(
                    url_put,{
                        'name':'testNameDocument',
                        'file': file
                    },
                    HTTP_AUTHORIZATION = f'Token {self.token_user2[0]}'
                )
            self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise AssertionError('O teste não foi executado, devido a falha na criação do documento')
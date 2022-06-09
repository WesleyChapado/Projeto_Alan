from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserModel
from rest_framework.authtoken.models import Token
import requests

class DocumentEndpointsTests(APITestCase):
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

    def test_post_create_document(self):
        '''
            Cria um documento para o usuário 1
        '''
        url = '/v1.0/register/document/'
        data = {
            "name": "testNameDocument"
        }
        files=[
            ('file',('file',open('corev1/tests/pdf_1_pagina.pdf','rb'),'application/pdf'))
        ]
        response = self.client.post(
            url, 
            data=data,
            files=files,
            format="json",
            HTTP_AUTHORIZATION = f'Token {self.token_user1[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # url = "http://localhost:8000/v1.0/register/document/"
        # payload={'name': 'Documento 1'}
        # files=[
        #     ('file',('file',open('corev1/tests/pdf_1_pagina.pdf','rb'),'application/pdf'))
        # ]
        # headers = {
        #     'Authorization':f'Token {self.token_user1[0]}'
        # }
        # print('********************')
        # print(headers)
        # print('********************')
        # response = requests.request("POST", url, headers=headers, data=payload, files=files)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        

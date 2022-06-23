from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserModel
from rest_framework.authtoken.models import Token

class OrganizationEndpointsTests(APITestCase):
    def setUp(self):
        '''
            Cria um usuário para ser usado nos próximos testes
        '''
        self.user = UserModel.objects.create(
            username= "testUsername",
            first_name= "testFN",
            last_name= "testLN",
            email= "test@gmail.com",
            password= "1234aB",
            organization= "testOrganization1",
        )
        self.token_user = Token.objects.get_or_create(user=self.user)
    
    def test_get_lista_organization(self):
        '''
            Lista todas as organizações, um token deve ser informado no HEADER
        '''
        url = '/v1.0/register/organization/'
        response = self.client.get(
            url, 
            format='json', 
            HTTP_AUTHORIZATION = f'Token {self.token_user[0]}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
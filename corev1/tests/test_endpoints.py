from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from corev1.organization.views import OrganizationView
from corev1.plan.views import PlanView
from user.models import UserModel
from rest_framework.test import APIRequestFactory
from user.views import UserList

class EndpointsTests(APITestCase):
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
            organization= "UT",
        )
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
        view = UserList.as_view()
        request = APIRequestFactory().get('/v1.0/register/user/list/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lista_organization(self):
        '''
            Lista todas as organizações, um token deve ser informado no HEADER
        '''
        view = OrganizationView.as_view()
        request = APIRequestFactory().get('v1.0/register/organization/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_lista_plans(self):
        '''
            Lista todos os planos, um token deve ser informado no HEADER
        '''
        view = PlanView.as_view()
        request = APIRequestFactory().get('/v1.0/register/plan/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

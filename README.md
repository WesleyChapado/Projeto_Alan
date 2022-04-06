# Projeto Alan
Um projeto de treinamento criado por Marco Oliveira.

## 📋Requisitos do pojeto
* Ambiente virtual (VENV)
* Docker
* Docker Compose
* Python
* Git
  
## 🔧 Instalação
Crie e inicie seu ambiente virtual
```bash
python3 -m venv ./venv
. venv\bin\activate
```
Faça as migrações para o container do postgresql
```bash
docker-compose run web python3 manage.py makemigrations corev1
docker-compose run web python3 migrate
```
Crie o superuser
```bash
docker-compose run web python3 manage.py createsuperuser
```
Inicie o container do projeto/postgresql com com todas suas dependências
```bash
docker-compose up
```
## 🔗Links para envio de requests
* localhost:8000/v1.0/register/user
* localhost:8000/v1.0/register/organization
  
  Até o momento atual do projeto apenas requests do tipo GET e POST são permitidas

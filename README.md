# django-microservices demo
Django Microservices testbed for some use cases:
* Frontend connects to single backend
* Frontend connects to multiple backens directly
* Frontend connects to multiple backens through Service gateway

## Frontend connects to single backend

### Deploy on Backend
* git clone https://github.com/latuannetnam/django-microservices.git
* cd django-microservices/frontend-single-backend/djbackend
* pip3 install -r requirements.txt
* python3 manage.py makemigrations polls
* python3 manage.py migrate
* python3 manage.py createsuperuser --email admin@example.com --username admin
  * Superuser: admin/xxxx
* cd djbackend
* Edit settings.py
  * ALLOWED_HOSTS = ['backend_ip']
* python3 manage.py runserver 0.0.0.0:8000
* API URL:http://backend_ip:8000
* Admin URL:http://backend_ip:8000/admin

### Deploy on Frontend
* git clone https://github.com/latuannetnam/django-microservices.git
* cd django-microservices/frontend-single-backend/djfrontend
* pip3 install -r requirements.txt
* cd djfrontend
* Edit settings.py
``` python
 ALLOWED_HOSTS = ['frontend_ip']
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'api': {
        'ENGINE': 'rest_models.backend',
        'NAME': 'http://backend:8000/',
        # 'USER': 'admin',
        # 'PASSWORD': 'xxxx',
        # 'AUTH': 'rest_models.backend.auth.BasicAuth',
    },
}
```
* cd ..
* python3 manage.py migrate
* python3 manage.py createsuperuser --email admin@example.com --username admin
  * Superuser: admin/xxxx
* python3 manage.py runserver 0.0.0.0:8000
* Admin URL:http://frontend_ip:8000/admin



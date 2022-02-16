import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


#SQL LITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dba_ecommerce',
        'USER': 'ecommerce',
        'PASSWORD': 'ecommerce',
        'HOST': 'ecommerce_db',
        'PORT': '3306',
    }
}
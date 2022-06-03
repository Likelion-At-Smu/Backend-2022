
# SECURITY WARNING: keep the secret key used in production secret!
mySECRET_KEY = 'django-insecure---2e%&v=!e247c0ppb17rsxximbik5m(*^i1%7&tne=b5u9gpc'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# pip install mysqlclient
myDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'mysql',
        'USER': 'root',
        'PASSWORD':'1320',
        'HOST': '127.0.0.1',
        'PORT':'3307',
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}


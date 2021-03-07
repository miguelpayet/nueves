import os
from pathlib import Path

ALLOWED_HOSTS = ["192.168.1.218", "localhost"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
LANGUAGE_CODE = 'es'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = False
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_L10N = True
USE_TZ = True
X_FRAME_OPTIONS = 'DENY'

STATIC_ROOT = os.path.join(BASE_DIR, '../revista_app/static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'uuubuntu',
        'NAME': 'nn',
        'PASSWORD': 'poq38uasldkvn',
        'USER': 'nn',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

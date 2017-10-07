from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 've%9v-0#d9bprtr-a_ck_@ee&s@r$f_3dtl+tqpz&l1sldn402'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['192.168.2.10']
INSTALLED_APPS += [
    'django_extensions',
]

# Wagtail settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'dev_media')

try:
    from .local import *
except ImportError:
    pass

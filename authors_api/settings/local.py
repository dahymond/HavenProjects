from .base import * #noqa
from .base import env

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default ="BPvSQ-U45L_3uzPkxXJSxoMnUnOkXevhaM5MlIE9RFqFYqNgGrY", 
) 

#SECURITY WARNING: don't run with debug turned on in production!
DEBUG=True

CSRF_TRUSTED_ORIGINS = ["http://locahost:8080"]
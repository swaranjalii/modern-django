from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default=')8c=0g_v7zc**oql165jqcg!6r60aad80t$gbcep@1g6g#kz6q')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
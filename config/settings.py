"""
Django settings for minimal transcription starter.

No database, no migrations, no Django admin - just API endpoints.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = ['*']

PORT = int(os.environ.get('PORT', 8081))
HOST = os.environ.get('HOST', '0.0.0.0')
FRONTEND_PORT = int(os.environ.get('FRONTEND_PORT', 8080))

# Application definition
INSTALLED_APPS = [
    'daphne',  # Must be first for Channels
    'corsheaders',
    'starter',
    'channels',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'
ASGI_APPLICATION = 'config.asgi.application'

DATABASES = {}

CORS_ALLOWED_ORIGINS = [
    f"http://localhost:{FRONTEND_PORT}",
    f"http://127.0.0.1:{FRONTEND_PORT}",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

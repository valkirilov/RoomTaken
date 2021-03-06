"""
Django settings for codebase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e9i#%hvb+q#9f-gwumg8#$ad6zot#)i9p1&0vm9hc1&j_tz((9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

AUTH_USER_MODEL='auth.User'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'corsheaders',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'south',
    'rest_framework',
    'api',
    'rest_framework.authtoken',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

# Add cors haders
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
       'GET',
       'POST',
       'PUT',
       'PATCH',
       'DELETE',
       'OPTIONS'
   )

CORS_ALLOW_HEADERS = (
   'x-requested-with',
   'content-type',
   'accept',
   'origin',
   'authorization',
   'x-csrftoken'
)

ROOT_URLCONF = 'codebase.urls'

WSGI_APPLICATION = 'codebase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

TEMPLATE_CONTEXT_PROCESSORS = (
 'django.contrib.auth.context_processors.auth',
 'django.core.context_processors.debug',
 'django.core.context_processors.i18n',
 'django.core.context_processors.media',
 'django.core.context_processors.static',
 'django.core.context_processors.tz',
 'django.core.context_processors.request',
 'django.contrib.messages.context_processors.messages',
 )


REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
        
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.AllowAny',
    ),
                  
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ]
}

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'room_taken',
            'USER': 'root',
            'PASSWORD': 'parola',
            'HOST': '/opt/lampp/var/mysql/mysql.sock',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
           
    '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
}

try:
    from local_settings import *
except ImportError, exp:
    pass

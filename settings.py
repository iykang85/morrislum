import os
import socket

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jack Hsu', 'jack.hsu@gmail.com'),
    ('Morris Lum', 'morrislum@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'morrislum.db'             # Or path to database file if using sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Canada/Toronto'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
#MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_ROOT = '/home/morrislum/webapps/static'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
ADMIN_MEDIA_PREFIX = '/static/admin/'

FIXTURE_DIRS = (
    os.path.join(SITE_ROOT, 'fixtures'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b%rja4o=ghv0^lh57h5r(_t@*9ky6fjun@m)q0cib-5hr@o=6v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'morris.middleware.SetRemoteAddrFromForwardedFor',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'tagging',
    'photologue',
    'django.contrib.markup',
    'django.contrib.comments',
    'main',
    'blog',
)

# Photologue
GALLERY_SAMPLE_SIZE = 6

try:
    from local_settings import *
except ImportError:
    pass


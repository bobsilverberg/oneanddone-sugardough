# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

# To extend any settings from settings/base.py here's an example:
# INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

import base


# django-debug-toolbar

MIDDLEWARE_CLASSES = base.MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

JINGO_EXCLUDE_APPS = base.JINGO_EXCLUDE_APPS + [
    'debug_toolbar',
]

INTERNAL_IPS = ('127.0.0.1', )

# django-browserid auto-login

# AUTHENTICATION_BACKENDS = ('django_browserid.auth.AutoLoginBackend',) + \
#                           base.AUTHENTICATION_BACKENDS
# BROWSERID_AUTOLOGIN_EMAIL = 'bsilverberg@mozilla.com'
# BROWSERID_AUTOLOGIN_ENABLED = True
#
# MINIFY_BUNDLES = base.MINIFY_BUNDLES
# MINIFY_BUNDLES['js']['base'] += ('browserid/autologin.js',)


# # Environment-specific Settings
# ##############################################################################
#
# # Is this a development instance? Set this to True on development/master
# # instances and False on stage/prod.
# DEV = True
#
# # Should robots.txt allow web crawlers? Set this to True for production
# ENGAGE_ROBOTS = True
#
# # django-browserid requires you to specify audiences that are valid for your
# # site. An audience is a protocol + hosename + port that users will use to
# # access your site.
# #
# # In development, this is typically 'http://localhost:8000' or similar. In
# # production, this is typically the protocol and domain for the site.
# BROWSERID_AUDIENCES = ['http://localhost:8000', 'http://127.0.0.1:8000']
#
# # Path to lessc binary (can be `lessc` if it's already on your path).
# # This isn't used if TEMPLATE_DEBUG is True.
# LESS_BIN = 'lessc'
#
#
# # Error Reporting
# ##############################################################################
#
# # Recipients of traceback emails and other notifications.
# ADMINS = (
#     ('One and Done Admin', 'bsilverberg@mozilla.com'),
# )
# MANAGERS = ADMINS
#
#
# # Security
# ##############################################################################
#
# # Playdoh ships with Bcrypt+HMAC by default because it's the most secure.
# # To use bcrypt, fill in a secret HMAC key. It cannot be blank.
# HMAC_KEYS = {
#     '2012-06-06': 'some secret',
# }
#
# from django_sha2 import get_password_hashers
# PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)
#
# # Make this unique, and don't share it with anybody. It cannot be blank.
# SECRET_KEY = 'bob'
#
#
# # Logging
# ##############################################################################
#
# # try:
# #     len(LOGGING)
# # except NameError:
# #     LOGGING = {}
# #
# # SYSLOG_TAG = "oneanddone_app"
# # LOGGING.setdefault('loggers', {})['playdoh'] = {
# #     'level': logging.DEBUG
# # }
#
#
# # LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))
# #
# # # Common Event Format logging parameters
# # CEF_PRODUCT = 'Playdoh'
# # CEF_VENDOR = 'Mozilla'
#
# # Email settings
# # To use the dummy smtp server, start it with
# # python -m smtpd -n -c DebuggingServer localhost:1025
# EMAIL_PORT = '1025'
# # EMAIL_HOST = 'smtp.mozilla.org'
# # SERVER_EMAIL= 'dev@oneanddone.allizom.org'
#
# # Caching
# CACHES = {
#     'default': {
#         'BACKEND': 'caching.backends.locmem.CacheClass',
#         'TIMEOUT': 60,
#     },
# }
#
# # CACHES = {
# #     'default': {
# #         'BACKEND': 'caching.backends.memcached.MemcachedCache',
# #         'LOCATION': '127.0.0.1:11211',
# #         'TIMEOUT': 600,
# #     }
# # }
#

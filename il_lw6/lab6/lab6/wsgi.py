"""
WSGI config for lab6 project.

It exposes the WSGI callable as a module-level variable named ``AuthorsBooks``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_AuthorsBooks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab6.settings')

AuthorsBooks = get_wsgi_AuthorsBooks()

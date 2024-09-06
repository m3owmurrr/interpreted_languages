"""
ASGI config for lab6 project.

It exposes the ASGI callable as a module-level variable named ``AuthorsBooks``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_AuthorsBooks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab6.settings')

AuthorsBooks = get_asgi_AuthorsBooks()

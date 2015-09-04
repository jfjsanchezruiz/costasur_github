"""
WSGI config for portal_cs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_cs.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

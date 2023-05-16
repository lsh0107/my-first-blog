"""
WSGI config for project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application
#from django.contrib.staticfiles.handlers import StaticFilesHandler



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')



application = get_wsgi_application()

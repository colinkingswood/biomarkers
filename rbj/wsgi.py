"""
WSGI config for rbj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
# import os
# 
# from django.core.wsgi import get_wsgi_application
# 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rbj.settings")
# 
# application = get_wsgi_application()

import os
import sys

path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'biomarkers.settings_pythonanywhere'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
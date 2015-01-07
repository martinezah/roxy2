import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

os.environ.setdefault('MEMEX_API_URL', '')
os.environ.setdefault('MEMEX_API_TOKEN', '')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

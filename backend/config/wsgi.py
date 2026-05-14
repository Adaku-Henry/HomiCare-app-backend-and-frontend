import os
from django.core.wsgi import get_wsgi_application

# Make sure 'config.' is removed from the settings path below
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
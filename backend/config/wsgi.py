import os
from django.core.wsgi import get_wsgi_application

# It MUST have the "config." prefix here
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
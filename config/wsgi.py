import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Create the WSGI application
application = get_wsgi_application()

# Vercel expects the handler to be named 'app'
app = application

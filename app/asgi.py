import os
from dotenv import load_dotenv

load_dotenv()

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.env.base')

application = get_asgi_application()

import sys
import os

project_path = '/home/safarito/domains/safari-tour.uz/public_html/core'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
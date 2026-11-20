# +--------------------------------------------------------------------------+
# | PythonAnywhere WSGI Configuration for Django                             |
# | Copy and paste the contents of this file into your PythonAnywhere        |
# | WSGI configuration file located at:                                      |
# | /var/www/<your-username>_pythonanywhere_com_wsgi.py                      |
# +--------------------------------------------------------------------------+

import os
import sys

# 1. Path to your cloned project repository on PythonAnywhere
# REPLACE '<your-username>' with your actual PythonAnywhere username:
path = '/home/<your-username>/Personal-Portfolio'
if path not in sys.path:
    sys.path.append(path)

# 2. Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

# 3. Import and set up the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

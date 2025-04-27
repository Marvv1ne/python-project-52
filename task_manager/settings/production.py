from .base import *
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
             'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
             }

LOCALE_PATHS = (
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 
                '..', "locale")),
)
print(os.environ.get('DATABASE_URL'))

from pathlib import Path
from dotenv import load_dotenv

from task_manager.settings.development import *

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-#31ik3$jzbqjd%+%n$@xs0h2@m*a95j+k1&h3em69ljlqeo&&i'

LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), "locale"),
)
print(LOCALE_PATHS)
from threading import Thread
import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
import django
import time


def upvotes_reset():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'test_task.settings')
    django.setup()
    from core.models import Upvote
    while True:
        time.sleep(60 * 60 * 24)
        Upvote.objects.all().delete()



Thread(target=upvotes_reset, daemon=True).start()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'test_task.settings')
application = get_wsgi_application()
call_command('runserver', '0.0.0.0:8000')

from celery.task import periodic_task
from datetime import timedelta
from .models import Upvote


@periodic_task(run_every=(timedelta(hours=24)), name="reset_upvotes")
def reset_upvotes():
    Upvote.objects.all().delete()

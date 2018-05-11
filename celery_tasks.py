import time
from celery_main import celery_app
from celery.schedules import crontab
from celery.task import periodic_task


@celery_app.task
def print_string_after_2s(string):
    print('Ready to print...')
    time.sleep(2)
    print('Print %s' % string)
    return 'Print Successful!'


@celery_app.task
def add(x, y):
    return x + y


@periodic_task(run_every=crontab(minute='*/2'))
def print_schdule_2mins():
    print_string_after_2s('periodic_task every 2 mins.')

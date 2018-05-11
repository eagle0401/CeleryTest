from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE = 'Asia/Taipei'
CELERYBEAT_SCHEDULE = {
    'print_every_30s': {
        'task': 'celery_tasks.print_string_after_2s',
        'schedule': timedelta(seconds=30),
        'args': ('task schedule', )
    },

    'print_schedule_crontab': {
        'task': 'celery_tasks.print_string_after_2s',
        'schedule': crontab(minute='*/1'),
        'args': ('task schedule crontab',)
    }
}

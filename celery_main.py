from celery import Celery

celery_app = Celery('tasks', include=['celery_tasks'])
celery_app.config_from_object('celery_config')



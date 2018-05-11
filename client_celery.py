import time
from celery_tasks import print_string_after_2s

print(print_string_after_2s.delay('task 1'))
answer = print_string_after_2s.delay('task 2')
start_time = time.time()


while True:
    print('wait for ready %.2f seconds' % (time.time() - start_time))
    if answer.ready():
        break
    time.sleep(0.5)

print(answer.get())

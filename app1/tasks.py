from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery_progress.backend import ProgressRecorder

from time import sleep 


@shared_task
def add(x, y):
    return x + y


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    final_dest_value = 5
    for i in range(final_dest_value):
        sleep(duration)
        progress_recorder.set_progress(i+1,final_dest_value,f'{i}th Iteration')
    return 'Done'
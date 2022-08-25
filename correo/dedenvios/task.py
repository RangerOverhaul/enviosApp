from __future__ import absolute_import, unicode_literals
from celery import shared_task
from dedenvios.models import *
import time

@shared_task
def add(num):
    for i in range(num):
        time.sleep(i)
        print("{} segundos ".format(i+1))


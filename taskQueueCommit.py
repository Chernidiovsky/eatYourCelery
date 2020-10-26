# -*- coding: utf-8 -*-
from celeryMain import taskForTest


for i in range(100):
    # task is randomly committed to each worker
    taskForTest.delay()
# -*- coding: utf-8 -*-
from celery import Celery
import time


broken_url = "redis://localhost:6379/0"
app = Celery("celeryTask", broker=broken_url, backend=broken_url)


@app.task
def taskForTest(i):
    print(i)
    time.sleep(1)


if __name__ == "__main__":
    # 清空上次的剩余任务
    app.control.purge()

    # 启动worker，配置并发数16
    app.worker_main(["worker", "-c", "16", "--loglevel=WARNING"])
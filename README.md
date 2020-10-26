# Eat your celery, son!
# celery + redis task queue demo


在架构上：

    [生产者] 包含很多个接口调用任务的脚本，所用函数必须在Celery主脚本中定义，并带上修饰符@app.task，并且使用.delay()来作为hook函数，等待worker调用
    
    [消息代理] 因为修饰符@app.task，任务提交给redis，形成一条任务队列
    
    [worker] redis把任务队列分配给Celery的各个worker同步并行

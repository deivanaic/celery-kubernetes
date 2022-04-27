from test_celery.tasks import longtime_add
import os
if __name__ == '__main__':
    url = [2,4,6,7,8]
    for i in url:
        queue_name = os.environ.get('QUEUE')
        print(queue_name)
        # Adding tasks to rabbitmq queue
        result = longtime_add.apply_async((i,),queue=queue_name)
        print('Task result:', result.get())
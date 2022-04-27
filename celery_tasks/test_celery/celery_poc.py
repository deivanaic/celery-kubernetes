from __future__ import absolute_import
from celery import Celery
# app = Celery('test_celery',broker='amqp://test:test@localhost:5672',backend='rpc://',include=['test_celery.tasks'])
app = Celery('test_celery',broker='amqps://ogcgpodt:MZjGWTJVKEcjina7N_qMkhSeEYj3hjQr@lionfish.rmq.cloudamqp.com/ogcgpodt',backend='rpc://',include=['test_celery.tasks'])
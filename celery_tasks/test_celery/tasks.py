
from __future__ import absolute_import
from test_celery.celery_poc import app

@app.task() # set a retry delay, 10 equal to 10s
def longtime_add(i):
    try:
        i = i+5
    except Exception:
        print("Error")
    return i
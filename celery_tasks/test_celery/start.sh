#!/bin/bash
echo "start.sh called"
echo ${DEPLOYMENT_TYPE}
echo ${QUEUE}
echo "celery -A test_celery.celery_poc worker --loglevel=info -Q ${QUEUE}"
if [[ "${DEPLOYMENT_TYPE}" == "Worker" ]]
then 
    celery -A test_celery.celery_poc worker --loglevel=info -Q ${QUEUE}
else
    echo "no matching command"
fi

# TODO - Add conditions for celery flower and celery beat and run them
exec "$@"
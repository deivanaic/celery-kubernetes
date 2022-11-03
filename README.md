# celery-kubernetes
Celery deployment on Kubernetes


Modern users expect pages to load instantaneously, but data-heavy tasks may take many seconds or even minutes to complete. How can we make sure users have a fast experience while still completing complicated tasks? 
If we want users to experience fast load times in our application, we’ll need to offload some of the work from our web server.

While we only have one or a handful of web servers responding to user requests, we can have many worker servers that process tasks in the background. We tell these workers what to do via a message queue. The queue ensures that each worker only gets one task at a time and that each task is only being processed by one worker.

Celery Tasks




Created a simple task to add numbers.
Queue name is obtained from env variables
apply_async((i,),queue=queue_name) -> Adds the task to Queue with argument i
Celery and rabbitmq servers are initialised. https://www.cloudamqp.com/ -> third party rabbitmq server.
Start.sh file is used to start the celery worker
Docker image is created using dockerfile. While setting up, run and check if docker image is up and running.


KUBE



Celery.yaml file -> creates a pod with the docker image.
Deployment_template.yaml -> provides a template for generating the deployments dynamically, env section specifies the queue name, deployment type, image name.
Generate_config.py reads the inputs from queue_details.yaml and replaces in the placeholders in the deployment_template to create the corresponding yaml files.
Startup.sh -> triggers the kubernetes to apply the deployments.



USEFUL COMMANDS

1.kubectl delete all --all
2. kubectl get pods
3. Kubectl exec -i -t <pod_name> - - bash
4. Python3 -m test_celery.run_tasks

TO-DO

1. celery flower and celery beat - deploy in Kubernetes with a command and deployment type.
2. Rediness and liveliness prob. - Need to check one thing, does kubernetes start the process automatically if it crashes

https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-liveness-probe

https://github.com/celery/celery/issues/4079#issuecomment-810975088
https://github.com/celery/celery/issues/4079#issuecomment-450679618







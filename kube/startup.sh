#!/bin/bash
out=$(kubectl get deployment | tail +2 | awk '{print $1}')
echo $out
for depl in $out
do
    echo $depl
done
python3 -m generate_config
yourfilenames=`ls deployment_*.yml`
for eachfile in $yourfilenames
do
   echo $eachfile
   envsubst < $eachfile | kubectl apply -f -
done

out=$(kubectl get deployment | tail +2 | awk '{print $1}')
echo $out
for depl in $out
do
    echo $depl
done
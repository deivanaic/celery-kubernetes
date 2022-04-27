import yaml

dataMap = ''
queue_config = ''

with open('queue_details.yaml') as f:
    # use safe_load instead load
    queue_config = yaml.safe_load(f)
    print(queue_config)

with open('deployment_template.yaml') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)
    spec = containers = dataMap.get('spec', {})
    containers = dataMap.get('spec', {}).get('template', {}).get('spec', {}).get('containers', {})

for key, value in queue_config.items():
    dataMap['metadata']['name'] = queue_config[key]['name']
    dataMap['metadata']['labels']['app'] = queue_config[key]['name']
    spec['selector']['matchLabels']['app'] = queue_config[key]['name']
    spec['template']['metadata']['labels']['app'] = queue_config[key]['name']
    containers[0]['name'] = queue_config[key]['name']
    containers[0]['env'][0]['value'] = key
    containers[0]['image'] = queue_config[key]['image']
    spec['replicas'] = queue_config[key]['no_of_workers']
    with open(f'deployment_{key}_generated.yml', 'w') as outfile:
        yaml.dump(dataMap, outfile, default_flow_style=False)


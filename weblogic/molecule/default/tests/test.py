import yaml

with open("../../../vars/main.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
        print config["dirs"]
    except yaml.YAMLError as exc:
        print(exc)

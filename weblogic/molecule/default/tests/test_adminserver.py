import os
import yaml
import testinfra.utils.ansible_runner

config_path = os.path.dirname(__file__)

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

with open("%s/flat.yml" % (config_path), 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


def test_nodemanager_service(host):
    for domain in config["domains"]:
        nodemanager = host.service("nodemanager_%s" % domain["name"])

        assert nodemanager.is_running
        assert nodemanager.is_enabled


def test_nodemanager_port(host):
    for domain in config["domains"]:
        nodemanager = host.socket("tcp://0.0.0.0:%s" % domain["nodemanager"]["port"])

        assert nodemanager.is_listening

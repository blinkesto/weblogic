import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

with open("../../vars/main.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


def test_nodemanager_service(host):
    nodemanager = host.service("nodemanager")

    assert nodemanager.is_running
    assert nodemanager.is_enabled


def test_nodemanager_port(host):
    nodemanager = host.socket("tcp://0.0.0.0:%s" % config["nodemanager"]["port"])

    assert nodemanager.is_listening

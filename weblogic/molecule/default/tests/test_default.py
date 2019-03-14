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


def test_java(host):
    java = host.package('%s' % config["java"]["package_name"])

    assert java.is_installed


def test_silent_xml(host):
    f = host.file('%s/silent.xml' % config["common"]["stage_dir"])

    assert f.exists


def test_nodemanager_service(host):
    nodemanager = host.service("nodemanager")

    assert nodemanager.is_running
    assert nodemanager.is_enabled

def test_nodemanagerport(host):
    nodemanager = host.socket("tcp://0.0.0.0:%s" % config["nodemanager"]["port"])

    assert nodemanager.is_listening

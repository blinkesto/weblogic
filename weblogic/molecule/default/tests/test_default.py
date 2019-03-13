import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

with open("../../vars/main.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
        print config["dirs"]
    except yaml.YAMLError as exc:
        print(exc)


def test_java(host):
    java = host.package('%s' % config["java"]["package_name"])

    assert java.is_installed


def test_install_jar(host):
    f = host.file('%s/%s' % (config["common"]["stage_dir"]),
                  config["weblogic"]["install"]["binary"])

    assert f.exists


def test_silent_xml(host):
    f = host.file('%s/silent.xml' % config["common"]["stage_dir"])

    assert f.exists

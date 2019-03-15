import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

with open("/Users/koydooley/PycharmProjects/molecule/weblogic/molecule/default/tests/flat.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


def test_java(host):
    java = host.package('%s' % config["java"]["package_name"])

    assert java.is_installed


def test_silent_xml(host):
    f = host.file('%s/silent.xml' % config["stage_dir"])

    assert f.exists




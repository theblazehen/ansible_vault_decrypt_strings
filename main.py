import sys

from ansible.parsing.vault import PromptVaultSecret, VaultLib, VaultSecret
from ruamel.yaml import YAML
from pprint import pprint

with open(sys.argv[1], "rb") as pw_file:
    pw = pw_file.read()

vault_pw = VaultSecret(pw)
vault_pw.load()

vl = VaultLib(secrets=[
    (None, vault_pw)
])

class VaultSecret:
    yaml_tag = u'!vault'

    def __init__(self, secret):
        self.secret = secret

    @classmethod
    def from_yaml(cls, constructor, node):
        return VaultSecret(vl.decrypt(node.value)).secret.decode('utf-8')

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.register_class(VaultSecret)


with open(sys.argv[2], 'r') as orig:
    y = yaml.load(orig)

with open(sys.argv[3], 'w') as dest:
    yaml.dump(y, dest)

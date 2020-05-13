import sys

from ansible.parsing.vault import PromptVaultSecret, VaultLib, VaultSecret, AnsibleVaultError
from ruamel.yaml import YAML
from pprint import pprint

if len(sys.argv) != 4:
    print("Supply <password_file> <input_yaml> <output_yaml>")
    exit(1)

try: 
    with open(sys.argv[1], "rb") as pw_file:
        pw = pw_file.read()
except FileNotFoundError:
    print("Password file not found")
    exit(1)

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


try:
    with open(sys.argv[2], 'r') as orig:
        try:
            y = yaml.load(orig)
        except AnsibleVaultError as e:
            print("Failed to decrypt")
            print(e)
            exit(1)
except FileExistsError:
    print(f"Failed to open {sys.argv[2]}")

with open(sys.argv[3], 'w') as dest:
    yaml.dump(y, dest)

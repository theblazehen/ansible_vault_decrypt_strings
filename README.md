# Decrypt values in yaml files that were encrypted with `ansible-vault encrypt_string`

## Add encrypted strings to your yaml file

Eg
```
something:
  test: $ANSIBLE_VAULT;1.1;AES256
          37363230323630386166393535343530313135646639616461666531303638346265393430613834
          3266363635316239356165616364366631363436316166390a313465323762376432306237366564
          66303132633533613463303965636535653965326133613133313030383232346435613063306335
          3562303938626232380a666333336164383931383236373437646665336166623862616130363764
          3239

```

## Save your password to a file

`echo -n hunter2 > vault_secret` be sure to add the `-n` so that you don't write a newline

## Decrypt the fields in your yaml file

### Create venv
`python -m venv ve && source ./ve/bin/activate`

### Run it

`python main.py vault_secret in.yaml out.yaml`

## Example pyinstaller usage
`pip install pyinstaller`
edit `main.spec` with your relative to venv paths
`./ve/bin/pyinstaller --onefile --hidden-import pkg_resources.py2_warn main.spec`
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/jeandre/Projects/work_lsd/old_mutual/vault_decrypt_strings'],
             binaries=[],
             datas=[
                 ("/home/jeandre/.virtualenvs/vault_decrypt_strings/lib/python3.8/site-packages/ansible/config/base.yml", "ansible/config"),
                 ("/home/jeandre/.virtualenvs/vault_decrypt_strings/lib/python3.8/site-packages/ansible/config/module_defaults.yml", "ansible/config")

             ],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

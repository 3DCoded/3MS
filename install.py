import os
from pathlib import Path
import shutil

install_files = '''
main.cfg
macros.cfg
KlipperScreen.conf
'''.strip().splitlines()

optional_files = '''
settings.cfg
variables.cfg
'''.strip().splitlines()

install_folders = '''
'''.strip().splitlines()

optional_folders = '''
controllers
'''.strip().splitlines()

from_dir = Path(os.path.dirname(__file__))
to_dir = Path.home() / 'printer_data' / 'config' / '3ms'

print(f'Installing from {from_dir} to {to_dir}')

def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy2(src, dst)

def install():
    os.makedirs(to_dir, exist_ok=True)
    for file in install_files:
        from_path = from_dir / file
        to_path = to_dir / file
        print(f'Installing file {file} to {to_path}')
        if os.path.exists(to_path):
            os.remove(to_path)
        shutil.copy2(from_path, to_path)
    for file in optional_files:
        from_path = from_dir / file
        to_path = to_dir / file
        print(f'Installing file {file} to {to_path}')
        if os.path.exists(to_path):
            continue
        shutil.copy2(from_path, to_path)
    for folder in install_folders:
        from_path = from_dir / folder
        to_path = to_dir / folder
        print(f'Installing folder {folder} to {to_path}')
        shutil.copytree(from_path, to_path, copy_function=copy, dirs_exist_ok=True)
    for folder in optional_folders:
        from_path = from_dir / folder
        to_path = to_dir / folder
        print(f'Installing folder {folder} to {to_path}')
        if os.path.exists(to_path):
            continue
        shutil.copytree(from_path, to_path, copy_function=copy, dirs_exist_ok=True)

if __name__ == '__main__':
    install()
    print('Successfully Installed 3MS')

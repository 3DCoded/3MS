import argparse
import os
import shutil
from pathlib import Path

install_files = '''
macros.cfg
endless/macros.cfg
cutter/macros.cfg
'''.strip().splitlines()

optional_files = '''
main.cfg
settings.cfg
variables.cfg
endless/settings.cfg
cutter/settings.cfg
'''.strip().splitlines()

install_folders = '''
'''.strip().splitlines()

optional_folders = '''
endless
cutter
controllers
controllers/btt_skr_mini_e3_v2
controllers/btt_octopus_main
controllers/einsy_rambo_with_skr_mini
controllers/zonestar_zm384_main
controllers/mini_rambo
controllers/btt_skr_pico
controllers/gtm32_103_v1
'''.strip().splitlines()

from_dir = Path(os.path.dirname(__file__))
to_dir = Path.home() / 'printer_data' / 'config' / '3ms'

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
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', nargs='?', const=str(to_dir), type=str, default=str(to_dir))
    args = parser.parse_args()
    to_dir = Path(args.path)
    print(f'Installing from {from_dir} to {to_dir}')
    install()
    print('Successfully Installed 3MS')

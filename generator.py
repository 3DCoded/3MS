"""
3MS Configuration Generator Script

Currently supports:
- URL-downloaded configuratios
- Main MCU configuration
- MMU MCU configuration
- Multi-MMU MCU configuration
- Per-stepper TMC driver selection

Currently does NOT spport:
- Local file configurations
- Configurations without TMC drivers
"""

import sys
import requests
import configparser

def format_pin(pin, mcu):
    prefixes = ''
    if '!' in pin: prefixes += '!'
    if '~' in pin: prefixes += '~'
    if '^' in pin: prefixes += '^'
    pin = pin.replace('!','').replace('~','').replace('^','')
    return f'{prefixes}{mcu}:{pin}'

def main():
    url = input('URL > ')
    resp = requests.get(url)

    if resp.status_code != 200: return 1

    config = resp.text
    updated_config = []
    in_section = False
    is_commented = False
    for line in config.splitlines():
        is_commented = False
        if line.startswith('#'):
            is_commented = True
            line = line[1:]
        if line.startswith('['):
            in_section = True
        if line.strip() == '' and in_section:
            in_section = False
        if is_commented and not in_section:
            line = f'#{line}'
        if in_section:
            updated_config.append(line)
        else:
            updated_config.append('\n')
    
    config = '\n'.join(updated_config)

    parser = configparser.RawConfigParser(strict=False, comment_prefixes=(';', '#'))
    parser.read_string(config)

    sections = parser.sections()
    stepper_sections = {}
    for section in sections:
        step_pin = parser.get(section, 'step_pin', fallback=None)
        dir_pin = parser.get(section, 'dir_pin', fallback=None)
        en_pin = parser.get(section, 'enable_pin', fallback=None)
        if step_pin and dir_pin and en_pin:
            stepper_sections[section] = {
                'stepper_conf': {
                    'step_pin': step_pin,
                    'dir_pin': dir_pin,
                    'enable_pin': en_pin,
                    'rotation_distance': 25,
                },
            }
    
    print('Available stepper options: ')

    i = 0
    stepper_keys = list(stepper_sections.keys())
    for key in stepper_sections:
        print(f'{i+1}) {key}')
        i += 1

    print('Please enter which steppers you want, seperated by spaces')
    desired_steppers_ids = [int(x) for x in input('Steppers > ').split()]
    desired_steppers_names = [stepper_keys[i-1] for i in desired_steppers_ids]

    desired_steppers = {}
    for key, value in stepper_sections.items():
        if key in desired_steppers_names:
            desired_steppers[key] = value
    
    for section in sections:
        if section.split()[-1] in desired_steppers:
            if 'tmc' in section:
                tmc_options = {}
                for option in parser.options(section):
                    tmc_options[option] = parser.get(section, option)

                desired_steppers[section.split()[-1]][section.split()[0]] = tmc_options
    
    tmc_selections = {}
    for name, data in desired_steppers.items():
        print(f'Stepper {name}: Which TMC driver will you use?')

        i = 0
        selection_opts = []
        for subdata in data:
            if 'tmc' in subdata:
                print(f'{i+1}) {subdata}')
                selection_opts.append(subdata)
                i += 1
        
        selection_id = int(input('Enter selection > '))
        selection_name = selection_opts[selection_id-1]

        tmc_selections[name] = selection_name
    
    
    print('Please enter the MCU name.\nIf this is an external mainboard, it should be "mmu".\nIf it is your existing mainboard, it should be blank.\nIf it is an additional mainboard to support extra steppers, it should be "mmu1", "mmu2", etc.')
    mcu_name = input('MCU Name > ').strip()

    if mcu_name != '':
        for name, data in desired_steppers.items():
            data['stepper_conf']['step_pin'] = format_pin(data['stepper_conf']['step_pin'], mcu_name)
            data['stepper_conf']['dir_pin'] = format_pin(data['stepper_conf']['dir_pin'], mcu_name)
            data['stepper_conf']['enable_pin'] = format_pin(data['stepper_conf']['enable_pin'], mcu_name)
            
            for opt, val in data[tmc_selections[name]].items():
                if 'pin' in opt:
                    data[tmc_selections[name]][opt] = format_pin(val, mcu_name)
            
    
    # ---------- mmu.cfg ----------
    writer = configparser.RawConfigParser(strict=False, comment_prefixes=(';', '#'), delimiters=(':',))
    
    i = 0
    for stepper, data in desired_steppers.items():
        stepper_name = f'stepper_mmu_gear_{i}' if i > 0 else 'stepper_mmu_gear'
        writer.add_section(stepper_name)
        for key, val in data['stepper_conf'].items():
            writer.set(stepper_name, key, val)
        
        tmc_section = f'{tmc_selections[stepper]} {stepper_name}'
        writer.add_section(tmc_section)
        for key, val in data[tmc_selections[stepper]].items():
            writer.set(tmc_section, key, val)
        
        i += 1
    
    with open('mmu_hardware.cfg', 'w') as file:
        writer.write(file)

    writer = configparser.RawConfigParser(strict=False, comment_prefixes=(';', '#'))
    if mcu_name:
        mcu_section = f'mcu {mcu_name}'
        writer.add_section(mcu_section)
        writer.set(mcu_section, 'serial', '/dev/serial/by-id/MCU-PATH')
    
    with open('mmu.cfg', 'w') as file:
        writer.write(file)
        if not mcu_name:
            file.write('# mmu.cfg can be empty, as this is a main MCU configuration')

if __name__ == '__main__':
    sys.exit(main())
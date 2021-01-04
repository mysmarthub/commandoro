#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Console utility for automatic command execution"""
import argparse
import inspect
import os
import shutil
import json
from pathlib import Path

VERSION = '0.0.6'


def smart_print(text='', char='-'):
    columns, _ = shutil.get_terminal_size()
    print(f'{text}'.center(columns, char))


def open_json(file):
    try:
        with open(file, 'r') as f:
            json_data = json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}
    else:
        return json_data


def executor(command: str, test=False):
    if not test:
        if type(command) is str:
            status = os.system(command)
            if status:
                return False
    return True


def createParser():
    parser = argparse.ArgumentParser(
        description='Utility for automatic command execution',
        prog=f'Commandoro',
        epilog="""The configuration file must be a file in the format
        json and have the correct settings.""",
    )
    parser.add_argument('--v', '--version', action='version', help='Program version',
                        version='%(prog)s v{}'.format(VERSION))
    parser.add_argument('path', nargs='?', help='Path to the settings file', default=False)
    return parser


def get_input():
    try:
        user_input = int(input('Enter the number to select: '))
    except ValueError:
        return -1
    else:
        return user_input


def get_pack_name(pack_dict):
    num_pack_dict = {n: name for n, name in enumerate(pack_dict.items(), 1)}
    smart_print('Command packages', '=')
    for n, val in num_pack_dict.items():
        name = val[0]
        command_list = val[1]
        print(f'{n}: {name} | commands: [{len(command_list)}]')
    smart_print()
    while True:
        user_input = get_input()
        if user_input in num_pack_dict:
            name = num_pack_dict[user_input][0]
            return name
        elif not user_input:
            return False
        else:
            print('Invalid input!!!')
            continue


def get_action():
    print(f'1 - Start\n'
          f'2 - List of commands\n'
          f'3 - Cancel')
    smart_print()
    return get_input()


def get_args(func):
    parser = createParser()
    namespace = parser.parse_args()
    if not namespace.path:
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        folder = os.path.dirname(os.path.abspath(filename))
        namespace.path = f'{folder}/commandoro/default_pack.json'
        if not Path(namespace.path).exists():
            namespace.path = f'{folder}/default_pack.json'

    def deco():
        smart_print('', '*')
        smart_print(f'Commandoro {VERSION}', '=')
        smart_print(' Aleksandr Suvorov | https://github.com/mysmarthub ', '-')
        smart_print(' Utility for automatic command execution ', '=')
        smart_print(' Donate: 4048 4150 0400 5852 ', '*')
        func(namespace)
        print()
        smart_print(' Donate: 4048 4150 0400 5852 ', '-')
        smart_print(' Copyright © 2020-2021 Aleksandr Suvorov ', '=')
        smart_print('Program completed', '-')
    return deco


def execute_the_command(command_list, test=False):
    count = 0
    errors = 0
    for command in command_list:
        count += 1
        print('\n')
        print(f'{count}. [Execute]: {command}')
        status = executor(command, test=test)
        if status:
            print('Successfully!')
        else:
            errors += 1
            print('Error! Command not executed!')
    smart_print('', '=')
    print(f'Completed. Successfully: [{len(command_list) - errors}] | Errors: [{errors}]\n')


@get_args
def main(namespace):
    path = namespace.path
    if path:
        json_data: dict = open_json(path)
        if json_data:
            try:
                while True:
                    smart_print()
                    print('Press Ctrl+C to exit...')
                    pack_name = get_pack_name(json_data)
                    while True:
                        msg = f' Selected {pack_name} | Commands: [{len(json_data[pack_name])}] '
                        if 'default' in json_data and pack_name != 'default':
                            msg += f'+ default commands [{len(json_data["default"])}]'
                        smart_print(msg, '=')
                        action = get_action()
                        if action == 1:
                            command_list = json_data[pack_name]
                            if 'default' in json_data and pack_name != 'default':
                                command_list += json_data['default']
                            execute_the_command(command_list, test=False)
                            break
                        elif action == 2:
                            smart_print()
                            print(f'Commands for {pack_name}:\n')
                            for command in json_data[pack_name]:
                                print(command)
                            print()
                            if 'default' in json_data and pack_name != 'default':
                                print(f'Commands for default pack:\n')
                                for command in json_data['default']:
                                    print(command)
                            smart_print()
                            continue
                        elif action == 3:
                            break
                        else:
                            print('Invalid input!!!')
                            continue
            except KeyboardInterrupt:
                print()
                print('Exit...')
            except TypeError:
                print('Type Error in json file...')
        else:
            print('Error in the configuration file!!!')
    else:
        print('Error! The path does not exist!')


if __name__ == '__main__':
    main()

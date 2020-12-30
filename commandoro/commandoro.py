#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Utility for automatic command execution"""
import argparse
import inspect
import os
import shutil
import json
from pathlib import Path

COLUMNS, _ = shutil.get_terminal_size()
VERSION = '0.0.5'


def open_json(file):
    try:
        with open(file, 'r') as f:
            json_data = json.load(f)
    except json.decoder.JSONDecodeError:
        return {}
    else:
        return json_data


def make_dict(json_data):
    data_dict = {name: commands for name, commands in json_data.items()}
    if data_dict:
        return data_dict
    return False


def execute_the_command(command: str):
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
    parser.add_argument('path', nargs='?', help='Path to the settings file', default=False)
    parser.add_argument('--v', '--version',
                        action='version',
                        help='Program version',
                        version='%(prog)s v{}'.format(VERSION))
    return parser


def get_args(func):
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.path:
        path = namespace.path
    else:
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path = os.path.dirname(os.path.abspath(filename))
        path = f'{path}/default_pack.json'

    def deco():
        print(''.center(COLUMNS, '*'))
        print('Commandoro'.center(COLUMNS, '='))
        print(' Aleksandr Suvorov | https://github.com/mysmarthub '.center(COLUMNS, '-'))
        print(f' Utility for automatic command execution '.center(COLUMNS, '='))
        print(' Donate: 4048 4150 0400 5852 '.center(COLUMNS, '*'))
        if path:
            func(path)
        else:
            parser.print_help()
        print(''.center(COLUMNS, '='))
        print('Program completed'.center(COLUMNS, '-'))
    return deco


def get_input():
    try:
        user_input = int(input('Enter the number to select, to exit enter 0: '))
    except ValueError:
        return -1
    else:
        return user_input


def get_pack_name(pack_dict):
    num_pack_dict = {n: name for n, name in enumerate(pack_dict.items(), 1)}
    print('Command packages'.center(COLUMNS, '='))
    for n, val in num_pack_dict.items():
        name = val[0]
        command_list = val[1]
        print(f'{n}: {name} | commands: [{len(command_list)}]')
    print(''.center(COLUMNS, '-'))
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


def start_execute(pack_dict):
    while True:
        command_list = []
        pack_name = get_pack_name(pack_dict)
        if pack_name:
            command_list += pack_dict[pack_name]
            if pack_name != 'default' and 'default' in pack_dict:
                command_list += pack_dict['default']
            if command_list:
                while True:
                    count = 0
                    errors = 0
                    print(f' Selected {pack_name} | Commands: [{len(command_list)}] '.center(COLUMNS, '='))
                    print(f'1 - Start\n'
                          f'2 - List of commands\n'
                          f'0 - Cancel')
                    print(''.center(COLUMNS, '-'))
                    user_input = get_input()
                    if user_input == 1:
                        for command in command_list:
                            count += 1
                            print('\n')
                            print(f'{count}. [Execute]: {command}')
                            status = execute_the_command(command)
                            if status:
                                print('Successfully!')
                            else:
                                errors += 1
                                print('Error! Command not executed!')
                        print(''.center(COLUMNS, '='))
                        print(f'Completed. Successfully: [{len(command_list) - errors}] | Errors: [{errors}]\n')
                        break
                    elif user_input == 2:
                        for command in command_list:
                            print(command)
                        continue
                    elif not user_input:
                        break
                    else:
                        print('Invalid input!!!')
                        continue
            else:
                print('Commands not found...')

        else:
            print('Getting out...')
            break


@get_args
def main(path):
    if Path(path).exists():
        json_data: dict = open_json(path)
        if json_data:
            pack_dict = make_dict(json_data)
            start_execute(pack_dict)
        else:
            print('Error in the configuration file!!!')
    else:
        print('Error! The path does not exist!')


if __name__ == '__main__':
    main()

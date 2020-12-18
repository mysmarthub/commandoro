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
VERSION = '0.0.2'


def check_path(path):
    if type(path) is str and Path(path).exists() and Path(path).suffix == '.json':
        return True
    return False


def open_json(file):
    with open(file, 'r') as f:
        json_data = json.load(f)
    return json_data


def execute_the_command(command: str):
    if type(command) is str:
        status = os.system(command)
        if not status:
            return True
    return False


def menu(conf_dict):
    print(''.center(COLUMNS, '*'))
    print('Configuration Settings'.center(COLUMNS, '='))
    print(''.center(COLUMNS, '-'))
    for n, val in conf_dict.items():
        name = val[0]
        command_list = val[1]
        print(f'{n}: {name} | commands: [{len(command_list)}]')
    print(''.center(COLUMNS, '-'))


def get_input():
    while True:
        try:
            user_input = int(input('Enter the number to select, to exit enter 0: '))
        except ValueError:
            print('Input Error!')
            continue
        else:
            return user_input


def start(conf_dict):
    while True:
        menu(conf_dict)
        conf_number = get_input()
        if not conf_number:
            print('Getting out...')
            break
        if conf_number not in conf_dict.keys():
            print('Invalid input!!!')
            continue
        fix_name, fix_list = conf_dict[conf_number]
        while True:
            print(f'Selected {fix_name}'.center(COLUMNS, '='))
            print(''.center(COLUMNS, '-'))
            print(f'1 - Start\n'
                  f'2 - List of commands\n'
                  f'0 - Cancel')
            print(''.center(COLUMNS, '-'))
            user_input = get_input()
            if user_input == 1:
                for fix in fix_list:
                    print('\n')
                    print(f'Execute: {fix}'.center(COLUMNS, '-'))
                    print(f'[Execute]: {fix}')
                    print(f'Execute: {fix}'.center(COLUMNS, '-'))
                    status = execute_the_command(fix)
                    print(''.center(COLUMNS, '-'))
                    if status:
                        print('Successfully!')
                    else:
                        print('Error! Command not executed!')
                break
            elif user_input == 2:
                for fix in fix_list:
                    print(fix)
                continue
            break


def createParser():
    parser = argparse.ArgumentParser(
        description='Utility for automatic command execution',
        prog=f'Commandoro',
        epilog="""The configuration file must be a file in the format 
        .json and have the correct settings""",
    )
    parser.add_argument('path', nargs='?', help='Path to the settings file', default=False)
    parser.add_argument('--v', '--version',
                        action='version',
                        help='Program version',
                        version='%(prog)s v{}'.format(VERSION))
    return parser


def logo(func):
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace)
    if namespace.path:
        path = namespace.path
    else:
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path = os.path.dirname(os.path.abspath(filename))
        path = f'{path}/config.json'

    def deco():
        print(''.center(COLUMNS, '*'))
        print('Commandoro'.center(COLUMNS, '='))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print(f'Utility for automatic command execution'.center(COLUMNS, '='))
        if path:
            func(path)
        else:
            parser.print_help()
        print(''.center(COLUMNS, '='))
        print('Program completed'.center(COLUMNS, '-'))
    return deco


@logo
def main(path):
    if check_path(path):
        try:
            config = open_json(path)
        except json.decoder.JSONDecodeError as err:
            print(''.center(COLUMNS, '-'))
            print('Error in the configuration file!!!')
            print(f'Error: {err}')
        else:
            config_dict = {n: name for n, name in enumerate(config.items(), 1)}
            if config_dict:
                start(config_dict)
            else:
                print('Settings not found!')
    else:
        print('Error! The path does not exist!')


if __name__ == '__main__':
    main()

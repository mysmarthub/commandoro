#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Console utility for automatic command execution

The console version allows you to run a script in the terminal,
passing it a file with settings as an argument,
or use the default file. In the process, you select the desired
command package, then you can start execution,
display a list of commands for this package,
or return to the selection of the command package.
After executing all the commands,
the program goes to the main menu and again waits for
input to select the desired package, or exit the program.
"""
import argparse
import inspect
import os
import shutil
import json
from pathlib import Path

VERSION = '0.0.6'


def smart_print(text: str = '', char: str = '-'):
    """
    Prints text to the console in the center of the line

    - Prints based on changing the width of the terminal

    :param text: <str> The string to be output
    :param char: <str> Placeholder character
    :return: <None>
    """
    columns, _ = shutil.get_terminal_size()
    print(f'{text}'.center(columns, char))


def open_json(file: str) -> dict:
    """
    Open the settings file in json format.

    :param file: <str> Path to the file in json format with command packages
    :return: <dict> Dictionary with command packages, where the key is the name of the package,
        and the value is a list of commands. If an error occurs, it returns an empty dictionary.
    """
    try:
        with open(file, 'r') as f:
            json_data = json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}
    else:
        return json_data


def executor(command: str, test: bool = False) -> bool:
    """
    Executes the command

    :param command: <str> Command to execute
    :param test: <bool> Used for testing. True disables the actual execution of commands.
    :return: <bool> Logical status of command execution
    """
    if not test:
        if type(command) is str:
            status = os.system(command)
            if status:
                return False
    return True


def get_input() -> int:
    """
    Accepts input of digits from the user

    :return: <int> If the user entered a non-number,
        it returns -1, otherwise the number entered by the user
    """
    try:
        user_input = int(input('Enter the number to select: '))
    except ValueError:
        return -1
    else:
        return user_input


def get_action() -> int:
    """
    Display the command selection menu, get input

    :return: <int>  The number entered by the user
    """
    print(f'1 - Start\n'
          f'2 - List of commands\n'
          f'3 - Cancel')
    smart_print()
    return get_input()


def execute_the_command(command_list: iter, test: bool = False):
    """
    Execute a list of commands

    - display information about the command
    - the status of its execution
    - the command number
    - information about errors that have occurred

    :param command_list: <iter> Iterator containing strings with commands
    :param test: <bool> Used for testing. True disables the actual execution of commands.
    :return: <None>
    """
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


def get_pack_name(pack_dict: dict) -> str:
    """
    Displays command packages with the name of the package

    and the number of commands in each package.
    Accept input from the user, define and return the name of
    the selected command package.

    :param pack_dict: <dict> Correct dictionary with command packages
        where the key is the name of the package,
        the value is a list of commands.
    :return: <str> Name of the selected command package
    """
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
        else:
            print('Invalid input!!!')
            continue


def createParser() -> argparse.ArgumentParser:
    """
    Creating a command-line argument parser

    :return: <argparse.ArgumentParser> argument parser
    """
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


def get_args(func):
    """
    Decorator for the main function

    * create a parser
    * get argument
    * process the resulting path to the file with command packages
    * if the path is not found, try to use the default file
    * display information at the start and at the end

    :param func: <function> Function for decoration
    :return: <decorator>
    """
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
        smart_print(f' Commandoro {VERSION} ', '=')
        smart_print(' Aleksandr Suvorov | https://github.com/mysmarthub ', '-')
        smart_print(' Utility for automatic command execution ', '=')
        smart_print(' Donate: 4048 4150 0400 5852 ', '*')
        func(namespace)
        print()
        smart_print(' Donate: 4048 4150 0400 5852 ', '-')
        smart_print(' Copyright © 2020-2021 Aleksandr Suvorov ', '=')
        smart_print('Program completed', '-')
    return deco


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
                        msg = f'Selected {pack_name} | Commands: [{len(json_data[pack_name])}] '
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

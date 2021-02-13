#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/commandoro/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
import inspect
import json
import os
import shutil
from pathlib import Path


HOME = str(Path.home())


DEFAULT_JSON_DATA = {
    "New Name":
        [
            "new command",
            "other command"
        ],
    "default":
        [
            "new command",
            "other command"
        ]
}


class Pack:
    def __init__(self, name, command_list):
        self.name = name
        self.command_list = command_list

    @property
    def count(self):
        return len(self.command_list)


def get_root_path(file_name):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    folder = os.path.dirname(os.path.abspath(filename))
    path = os.path.join(folder, file_name)
    return path


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


def open_json_file(file):
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


def smart_print(text='', char='-'):
    if not char:
        char = ' '
    columns, _ = shutil.get_terminal_size()
    if text:
        print(f' {text} '.center(columns, char))
    else:
        print(f''.center(columns, char))


def create_file(file_name='', root=False):
    if not file_name:
        file_name = 'config.json'
    if root:
        root_path = get_root_path(file_name)
    else:
        root_path = os.path.join(HOME, file_name)
    with open(root_path, 'w') as f:
        json.dump(DEFAULT_JSON_DATA, f, indent=4)
    return root_path

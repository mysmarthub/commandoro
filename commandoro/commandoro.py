#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/commandoro/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Cli utility for automatic command execution"""

import click

try:
    from commandoro import settings, commander
except ImportError:
    import settings
    import commander


def start_logo():
    commander.smart_print('', '*')
    commander.smart_print(f'{settings.TITLE} v{settings.VERSION}', '=')
    commander.smart_print(f'{settings.DESCRIPTION}', '-')
    commander.smart_print()


def end_logo():
    commander.smart_print(f'{settings.YANDEX}', '-')
    commander.smart_print(f'{settings.COPYRIGHT}', '=')
    commander.smart_print('', '*')


def get_pack_name(file, pack_objects: dict):
    num_pack = {n: name for n, name in enumerate(pack_objects.keys(), 1)}
    while 1:
        """Shows a simple menu."""
        commander.smart_print('File information')
        click.echo(f'File: [{file}]')
        commander.smart_print('Command packages:')
        for n, name in num_pack.items():
            click.echo(f'{n}. {name} | Commands[{pack_objects[name].count}]')
        commander.smart_print()
        num = click.prompt(text='Enter the package number and click Enter (ctrl+c for exit)', type=int)
        if num not in num_pack:
            commander.smart_print()
            click.echo('Input Error!')
            input('Enter for continue ...')
            continue
        pack_name = num_pack[num]
        command_list = pack_objects[pack_name].command_list
        while 1:
            commander.smart_print()
            click.echo(f'The selected package {num_pack[num]} | '
                       f'Commands:[{pack_objects[pack_name].count}]')
            commander.smart_print()
            click.echo('1. Start')
            click.echo('2. Show commands')
            click.echo('3. Cancel')
            commander.smart_print()
            user_input = click.prompt(text='Enter the desired number and press ENTER', type=int)
            commander.smart_print()
            if user_input not in (1, 2, 3):
                click.echo('Input Error!')
                input('Enter for continue ...')
            elif user_input == 1:
                return pack_name
            elif user_input == 2:
                click.echo()
                click.echo(f'{pack_name} commands: ')
                for command in command_list:
                    click.echo(command)
                continue
            break


def start(pack_obj):
    count = 0
    errors = []
    click.echo()
    click.echo(f'Pack name: [{pack_obj.name}]')
    commander.smart_print()
    for command in pack_obj.command_list:
        count += 1
        click.echo()
        msg = f'[execute {count}]: {command}'
        click.echo(msg)
        status = commander.executor(command)
        if status:
            click.echo('[Successfully]')
        else:
            errors.append(f'Error: {msg}')
            click.echo('[Error]')
        commander.smart_print()
    commander.smart_print('', '=')
    click.echo(f'The command package [{pack_obj.name}] is executed.')
    click.echo(f'Commands completed: [{count - len(errors)}] | Errors: [{len(errors)}]')


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{settings.TITLE} {settings.VERSION} - {settings.COPYRIGHT}')
    ctx.exit()


@click.command()
@click.option('--file', '-f', help='The path to the file with the command packs',
              type=click.Path(exists=True, dir_okay=False))
@click.option('--default', '-d', is_flag=True, help='Run an additional batch of commands from default')
@click.option('--name', '-n', help='Name of the package to run automatically')
@click.option('--version', '-v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
def cli(file, default, name):
    """Commandoro - CLI utility for automatic command execution

    and auto-tuning Linux distributions after installation.

    - To work, the utility uses files that store named command packages,
        where the name is the name of the command package,
        and the value is a list of commands.

    - You can create your own files with command packages using
        default structure.

    - Use the name "default" for the package with the default commands.
        You can run them in addition to the selected batch of commands.

    - You can pass the file name as an argument
        or use the default file, it should be located
        in the same directory as the file being run.

    - The console version allows you to run the script in the terminal,
        passing it a file with the settings as an argument,
        or use the default file. In the process of working,
        you choose the right one command package,
        after which you can start executing, display a list
        of commands for this package,
        or go back to selecting the command package.

    - Using the -n or --name parameter, you can specify the name
        of the command package at startup,
        then the utility will immediately start automatic execution
        of commands from this package.

    - Examples of implementation:

    python commandoro.py --file config.json -d

    python commandoro.py --file config.json -d --name Ubuntu

    or

    commandoro --file config.json -d

    commandoro --file config.json -d --name Ubuntu

    """
    start_logo()

    while 1:
        if not file:
            click.echo('The file is not found...')
            commander.smart_print()
            click.echo('1. Open')
            click.echo('2. Create')
            click.echo('3. Edit')
            click.echo('0. Exit')
            commander.smart_print()
            prompt = click.prompt('Enter', type=int)
            commander.smart_print()
            if not prompt:
                break
            elif prompt == 1:
                file = click.prompt('File address', type=click.Path(exists=True, dir_okay=False))
            elif prompt == 2:
                while 1:
                    name = click.prompt('File name')
                    if len(name) < 4:
                        click.echo('Error! Name is too short!')
                        continue
                    break
                file = commander.create_file(name)
                click.edit(filename=file)
            elif prompt == 3:
                if not file:
                    file = click.prompt('File address', type=click.Path(exists=True, dir_okay=False))
                click.edit(filename=file)
                continue
        if file:
            pack_dict = commander.open_json_file(file)
            pack_objects = {key: commander.Pack(name=key, command_list=val) for key, val in pack_dict.items()}
            if pack_dict:
                if name and name in pack_dict:
                    pack_name = name
                else:
                    pack_name = get_pack_name(file=file, pack_objects=pack_objects)
                pack_obj = commander.Pack(pack_name, pack_dict[pack_name])
                start(pack_obj)
                if default and 'default' in pack_dict and pack_name != 'default':
                    pack_obj = commander.Pack(name='default', command_list=pack_dict['default'])
                start(pack_obj=pack_obj)
                break
            else:
                click.echo('No data available... There may be an error in the configuration file')
    end_logo()


if __name__ == '__main__':
    cli()

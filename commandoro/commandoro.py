# !/usr/bin/env python3
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


def end_logo():
    commander.smart_print(f'{settings.YANDEX}', '-')
    commander.smart_print(f'{settings.COPYRIGHT}', '=')
    commander.smart_print('', '*')


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{settings.TITLE} {settings.VERSION} - {settings.COPYRIGHT}')
    ctx.exit()


def open_file_dialog():
    file = click.prompt('File address', type=click.Path(exists=True, dir_okay=False))
    return file


def create_file_dialog():
    name: str = click.prompt('File name', type=str)
    name = name.replace(' ', '_')
    file = commander.create_file(f'{name}_commands.json', root=False)
    click.edit(filename=file)
    click.echo('The file is created in your home directory!')
    click.open_file(filename=file)
    return file


def edit_file_dialog(file=None):
    if file is None:
        file = click.prompt('File address', type=click.Path(exists=True, dir_okay=False))
    click.edit(filename=file)
    return file


def open_url(url):
    click.launch(url=url)


def get_file_menu():
    while 1:
        commander.smart_print('File menu')
        click.echo('o: open ')
        click.echo('c: create ')
        click.echo('e: edit ')
        click.echo('h: help ')
        click.echo('q: quit ')
        commander.smart_print()
        char = click.getchar()
        if char in ('q', 'й'):
            return 'exit'
        elif char in ('o', 'щ'):
            file = open_file_dialog()
        elif char in ('c', 'с'):
            file = create_file_dialog()
        elif char in ('e', 'у'):
            file = edit_file_dialog()
        elif char in ('h', 'р'):
            open_url(settings.README_URL)
            continue
        else:
            continue
        return file


def get_name_menu(pack_objects):
    num_pack = {n: name for n, name in enumerate(pack_objects.keys(), 1)}
    while 1:
        """Shows a simple menu."""
        commander.smart_print('Command packages:')
        for n, name in num_pack.items():
            click.echo(f'{n}: {name}: Commands:{pack_objects[name].count}')
        click.echo('0: open new file')
        commander.smart_print()
        num = click.prompt(text='Enter the package', type=int)

        if not num:
            return None

        if num not in num_pack:
            commander.smart_print()
            click.echo('Input Error!')
            input('Enter for continue ...')
            continue
        pack_name = num_pack[num]
        return pack_name


def get_action(title):
    while 1:
        click.echo(title)
        click.echo('y: yes')
        click.echo('n: no')
        char = click.getchar()
        if char == 'y':
            return True
        elif char == 'n':
            return False
        else:
            continue


def get_pack_action(pack_obj: commander.Pack):
    while 1:
        commander.smart_print('Pack menu')
        click.echo(f'The selected package: {pack_obj.name}({pack_obj.count})')
        commander.smart_print()
        click.echo('s: start')
        click.echo('p: print commands')
        click.echo('b. back')
        char = click.getchar()
        if char in ('b', 'и'):
            return False
        elif char in ('s', 'ы'):
            return True
        elif char in ('p', 'з'):
            commander.smart_print(f'{pack_obj.name} - commands:{pack_obj.count}')
            for n, command in enumerate(pack_obj.command_list, 1):
                click.echo(f'{n}. {command}')
            commander.smart_print()
            input('Enter for continue ... ')


def start(pack_obj, auto=True):
    count = 0
    errors = []
    click.echo()
    commander.smart_print(f'[name]:[{pack_obj.name}]')
    for command in pack_obj.command_list:
        commander.smart_print('', '=')
        count += 1
        msg = f'{count}: [execute]:{pack_obj.name}:{command}'
        click.echo(msg)
        if auto:
            work = True
        else:
            work = get_action('Do you want to continue?')

        if work:
            status = commander.executor(command)
            if status:
                click.echo('+ [Successfully!]')
            else:
                errors.append(f'Error: {msg}')
                click.echo('- [Error!!!]')
        else:
            click.echo('[Skipped...]')
    commander.smart_print('', '*')
    click.echo(f'The command package [{pack_obj.name}] is executed.')
    click.echo(f'Commands completed: [{count - len(errors)}] | Errors: [{len(errors)}]')


@click.command()
@click.option('--file', '-f', help='The path to the file with the command packs',
              type=click.Path(exists=True, dir_okay=False))
@click.option('--name', '-n', help='Name of the package')
@click.option('--auto', '-a', is_flag=True, help='Auto command execution, auto exit')
@click.option('--version', '-v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
def cli(file, name, auto):
    """Commandoro - CLI utility for automatic command execution.


    - Run the utility without parameters to manually select options.

    Example:
    commandoro
    python commandoro.py


    - Use the option -f/--file [filename] to select a file with command packages.

    Example:
    commandoro -f file.json
    python commandoro.py -f file.json


    - Use the option -n/--name to specify an existing package name.

    Example:
    commandoro -f file.json -n Ubuntu
    python commandoro.py -f file.json -n Ubuntu

    - Use the option -a for autorun and auto-completion.

    Example:
    commandoro -f file.json -n Ubuntu -a
    python commandoro.py -f file.json -n Ubuntu -a

    Author and developer: Aleksandr Suvorov

    Url: https://github.com/mysmarthub/

    Email: mysmarthub@ya.ru

    Donate: https://paypal.me/myhackband

    https://yoomoney.ru/to/4100115206129186

    4048 0250 0089 5923
        """
    start_logo()
    while file != 'exit':
        if file is None:
            commander.smart_print('File information')
            click.echo(f'File not found... ')
            file = get_file_menu()

        if file == 'exit':
            break

        if file:
            commander.smart_print('File information')
            click.echo(f'File: [{file}]')

            pack_dict = commander.open_json_file(file)

            if not pack_dict:
                click.echo('No data available... There may be '
                           'an error in the configuration file!')
                click.echo('Close file...')
                file = None
                continue

            pack_objects = {key: commander.Pack(name=key, command_list=val)
                            for key, val in pack_dict.items()}

            if name and name in pack_dict:
                pack_name = name
            else:
                pack_name = get_name_menu(pack_objects=pack_objects)

            if pack_name is None:
                file = None
                continue

            if name and name in pack_dict:
                action = True
            else:
                action = get_pack_action(pack_obj=pack_objects[pack_name])

            if action:
                commander.smart_print()
                click.echo(f'[pack name]:[{pack_name}]')
                click.echo('Getting started...')
                if not auto:
                    commander.smart_print()
                    sub_auto = get_action(title='Execute commands automatically?')
                else:
                    sub_auto = auto
                start(pack_obj=pack_objects[pack_name], auto=sub_auto)

                if auto:
                    file = 'exit'
                else:
                    commander.smart_print()
                    user_input = get_action('Close the program?')
                    if user_input:
                        break
                    else:
                        name = None
                        continue

            elif action is None:
                click.echo('\nExit...')
                break

            else:
                continue

    end_logo()


if __name__ == '__main__':
    cli()

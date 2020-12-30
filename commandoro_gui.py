#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Gui utility for automating the execution

of commands in different systems,
Create and edit your own files with command packages.
"""
import json
import os
import shutil
import sys
from pathlib import Path
import time

from PySide2 import QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QFileDialog, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton,
                               QCheckBox, QTextBrowser, QListWidget, QWidget, QAbstractItemView, QInputDialog,
                               QProgressBar)
from PySide2.QtCore import QThread, Signal

VERSION = '0.0.5'
# COLUMNS, _ = shutil.get_terminal_size()
COLUMNS = 60
LOG_NAME = 'commandoro_log.txt'


def open_json(file):
    try:
        with open(file, 'r') as f:
            json_data = json.load(f)
    except json.decoder.JSONDecodeError:
        return False
    else:
        return json_data


def execute_the_command(command: str):
    if type(command) is str:
        status = os.system(command)
        if status:
            return False
    return True


def make_dict(json_data):
    data_dict = {name: commands for name, commands in json_data.items()}
    if data_dict:
        return data_dict
    return False


class Exec(QThread):
    signal = Signal(str)
    signal2 = Signal(int)

    def __init__(self):
        super().__init__()
        self.log_status = False
        self.pack_name = 'Default'
        self.commands_pack = []
        self.commands = []
        self.errors = []

    def run(self):
        n = 0
        count = 0
        progress_step = 100/len(self.commands_pack)
        for command in self.commands_pack:
            n += 1
            count += progress_step
            self.send_emit(''.center(COLUMNS, '-'))
            self.send_emit(f'{n} [Execute] {command}')
            status = execute_the_command(command)
            if status:
                self.send_emit(f'Command completed successfully')
            else:
                self.errors.append(command)
                self.send_emit(f'Error executing the command!')
            self.signal2.emit(count)
        self.send_emit(''.center(COLUMNS, '-'))
        self.send_emit(f'The work has been completed. '
                       f'Executed commands: {len(self.commands_pack)} | '
                       f'Errors: {len(self.errors)}')
        self.send_emit(''.center(COLUMNS, '-'))
        if self.errors:
            self.send_emit('Errors:')
            for err in self.errors:
                self.send_emit(err)
        if self.log_status:
            self.make_log()

    def make_log(self):
        with open(LOG_NAME, 'a') as file:
            print(''.center(COLUMNS, '='), file=file)
            print(f'{self.pack_name}: '
                  f'{time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())}',
                  file=file)
            print(''.center(COLUMNS, '='), file=file)
            for msg in self.commands:
                print(msg, file=file)

    def send_emit(self, msg):
        if self.log_status:
            self.commands.append(msg)
        self.signal.emit(msg)

    def reset(self):
        self.commands_pack.clear()
        self.commands.clear()
        self.errors.clear()
        self.log_status = False
        self.pack_name = 'Default'


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.options_file = ''
        self.options_dict = dict()

        self.setWindowTitle('Commandoro - utility for automating the execution '
                            'of commands in different systems, Create and edit '
                            'your own files with command packages...')

        self.label_logo = QLabel(f'Commandoro<sup>{VERSION}</sup>')
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.label_logo.setStyleSheet('font-size: 48px;')

        self.label_console = QLabel('Information console:')
        self.text_console = QTextBrowser()
        self.text_console.setText(f'Welcome to the Utility for automating '
                                  f'the execution of commands in different systems, '
                                  f'сreate and edit your own files with command packages...')
        self.text_console.append(''.center(COLUMNS, '='))
        self.btn_show_help = QPushButton('Help')
        self.btn_console_clear = QPushButton('Clear the console')

        self.label_options = QLabel('Commands package: 0')

        self.list_options = QListWidget()

        self.btn_new_pack = QPushButton('+ Pack')
        self.btn_remove_pack = QPushButton('- Pack')
        self.btn_open_file = QPushButton('Open file')
        self.btn_edit_pack_name = QPushButton('Edit')
        self.btn_save_as = QPushButton('Save as')
        self.btn_save = QPushButton('Save')
        self.btn_reset = QPushButton('Reset')

        self.label_commands = QLabel('Commands: 0')
        self.list_commands = QListWidget()
        self.list_commands.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.label_default_commands = QLabel('Default commands:')
        self.list_commands_default = QListWidget()
        self.list_commands_default.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.label_donat = QLabel('Donate: 4048 4150 0400 5852')

        self.btn_command_add = QPushButton('+ Add')
        self.btn_command_remove = QPushButton('- Remove')
        self.btn_command_edit = QPushButton('Edit')

        self.btn_exec = QPushButton('Execute')
        self.btn_exit = QPushButton('Exit')

        self.ch_log = QCheckBox('Save log?')
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        self.h_box1 = QHBoxLayout()
        self.h_box1.addStretch()
        self.h_box1.addWidget(self.btn_show_help)
        self.h_box1.addWidget(self.btn_console_clear)

        self.v_box1 = QVBoxLayout()
        self.v_box1.addWidget(self.label_console)
        self.v_box1.addWidget(self.text_console)
        self.v_box1.addLayout(self.h_box1)

        self.h_box2 = QHBoxLayout()
        self.h_box2.addWidget(self.btn_open_file)
        self.h_box2.addWidget(self.btn_save)
        self.h_box2.addWidget(self.btn_save_as)
        self.h_box2.addWidget(self.btn_reset)
        self.h_box2.addStretch()
        self.h_box2.addWidget(self.btn_new_pack)
        self.h_box2.addWidget(self.btn_remove_pack)
        self.h_box2.addWidget(self.btn_edit_pack_name)

        self.v_box2 = QVBoxLayout()
        self.v_box2.addWidget(self.label_options)
        self.v_box2.addWidget(self.list_options)
        self.v_box2.addLayout(self.h_box2)

        self.h_box3 = QHBoxLayout()
        self.h_box3.addWidget(self.btn_command_add)
        self.h_box3.addWidget(self.btn_command_edit)
        self.h_box3.addWidget(self.btn_command_remove)
        self.h_box3.addStretch()

        self.v_box3 = QVBoxLayout()
        self.v_box3.addWidget(self.label_commands)
        self.v_box3.addWidget(self.list_commands)
        self.v_box3.addLayout(self.h_box3)

        self.v_box4 = QVBoxLayout()
        self.v_box4.addWidget(self.label_default_commands)
        self.v_box4.addWidget(self.list_commands_default)

        self.command_box = QHBoxLayout()
        self.command_box.addLayout(self.v_box3)
        self.command_box.addLayout(self.v_box4)

        self.h_box4 = QHBoxLayout()
        self.h_box4.addWidget(self.label_donat)
        self.h_box4.addSpacing(150)
        self.h_box4.addWidget(self.btn_exec)
        self.h_box4.addWidget(self.btn_exit)

        self.v_box4 = QVBoxLayout()
        self.v_box4.addLayout(self.h_box4)

        self.zero_box = QVBoxLayout()
        self.zero_box.addSpacing(30)

        self.h_box5 = QHBoxLayout()
        self.h_box5.addWidget(self.ch_log)
        self.h_box5.addWidget(self.progress_bar)

        self.default_box = QVBoxLayout()
        self.default_box.addWidget(self.label_logo)
        self.default_box.addLayout(self.v_box1)
        self.default_box.addLayout(self.v_box2)
        self.default_box.addLayout(self.command_box)
        self.default_box.addLayout(self.zero_box)
        self.default_box.addLayout(self.v_box4)
        self.default_box.addLayout(self.h_box5)

        self.setLayout(self.default_box)

        self.btn_console_clear.clicked.connect(self.clear_console)
        self.btn_show_help.clicked.connect(self.show_help)
        self.btn_exit.clicked.connect(self.close)
        self.btn_open_file.clicked.connect(self.open_options_file)
        self.btn_save_as.clicked.connect(self.save_as_options_file)
        self.btn_reset.clicked.connect(self.close_options_file)
        self.btn_command_remove.clicked.connect(self.remove_commands_item)
        self.btn_command_add.clicked.connect(self.add_command)
        self.btn_new_pack.clicked.connect(self.new_pack)
        self.btn_remove_pack.clicked.connect(self.remove_pack)
        self.btn_save.clicked.connect(self.save_option_file)
        self.btn_exec.clicked.connect(self.start_execute)
        self.btn_edit_pack_name.clicked.connect(self.edit_option_name)
        self.btn_command_edit.clicked.connect(self.edit_command)

        self.my_exec = Exec()

        self.my_exec.signal.connect(self.update_information)
        self.my_exec.signal2.connect(self.update_progress)
        self.my_exec.started.connect(self.at_start)
        self.my_exec.finished.connect(self.at_finish)

        self.list_options.itemSelectionChanged.connect(self.selectionChanged)
        self.get_default_file()
        self.update_label()

    def update_progress(self, n):
        self.progress_bar.setValue(n)

    def update_information(self, s: str) -> None:
        self.text_console.append(s)
        self.text_console.moveCursor(QtGui.QTextCursor.End)
        self.update_label()

    def show_msg(self, title: str = 'Warning!', msg: str = 'Message...') -> None:
        QMessageBox.about(self, title, msg)

    def update_label(self):
        self.label_commands.setText(f'Commands: {self.list_commands.count()}')
        if self.options_file:
            self.label_options.setText(f'Commands package: {len(self.options_dict)} | '
                                       f'File opened: {Path(self.options_file).name}')
        else:
            self.label_options.setText(f'Commands package: {len(self.options_dict)}')
        if not self.list_options.count():
            self.list_commands.clear()
            self.list_commands_default.clear()

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self,
                                     'Exit',
                                     'Are you sure you want to terminate the program?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hide()
            self.my_exec.wait(1000)
            event.accept()
        else:
            event.ignore()

    def show_help(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.clear_console()
        try:
            with open('README.md', 'r') as f:
                self.print_console(f.read())
        except FileNotFoundError:
            self.print_console('Error! Help file not found!')

    def clear_console(self):
        self.text_console.clear()
        self.text_console.setText(f'Welcome to the Utility for automating '
                                  f'the execution of commands in different systems, '
                                  f'сreate and edit your own files with command packages...')
        self.text_console.append(''.center(COLUMNS, '='))

    def print_console(self, msg):
        self.text_console.append(msg)

    def open_options_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path_tuple = QFileDialog.getOpenFileNames(self, 'Select files to add: ', options=options)
        if path_tuple[0]:
            for path in path_tuple[0]:
                self.open_file(path)
            self.print_console(''.center(COLUMNS, '-'))
            self.update_label()

    def close_options_file(self) -> None:
        self.options_dict.clear()
        self.list_options.clear()
        self.list_commands.clear()
        self.list_commands_default.clear()
        self.options_file = ''
        self.print_console('Reset is executed. When performing this function, '
                           'information in open files is not saved!')
        self.update_label()

    def save_as_options_file(self):
        # Bug!!!
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.save_file(file_name)

    def save_file(self, file):
        with open(file, 'w') as f:
            json.dump(self.options_dict, f)
            f.flush()
        self.show_msg(msg=f'File {file} successfully saved!')
        self.options_file = file
        self.update_label()

    def save_option_file(self):
        if self.options_file:
            self.save_file(self.options_file)
        else:
            self.save_as_options_file()

    def new_pack(self):
        c, s = QInputDialog.getText(self,
                                    'Input Dialog',
                                    'Enter the name of the new commands pack:',
                                    text='New pack name')
        if c and s:
            if c not in self.options_dict:
                self.options_dict[c] = []
                self.add_item(self.list_options, c)
            else:
                self.show_msg(msg='This name is already used!')
            self.update_label()

    def remove_pack(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            self.list_options.takeItem(self.list_options.row(item))
            del self.options_dict[item.text()]
            if item.text() == 'default':
                self.list_commands_default.clear()
        self.update_label()

    def edit_option_name(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            c, s = QInputDialog.getText(self, f'Rename {item.text()}?',
                                        'Enter a new name for the package: ',
                                        text=f'{item.text()}')
            if c and s and c not in self.options_dict:
                temp = self.options_dict[item.text()]
                del self.options_dict[item.text()]
                self.options_dict[c] = temp
                self.list_options.takeItem(self.list_options.row(item))
                self.add_item(self.list_options, c)

    def remove_commands_item(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            for SelectedItem in self.list_commands.selectedItems():
                self.list_commands.takeItem(self.list_commands.row(SelectedItem))
                self.options_dict[item.text()].remove(SelectedItem.text())
        self.update_label()

    def add_command(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            c, s = QInputDialog.getText(self, 'Input Dialog', 'Enter the command:',
                                        text=f'New command')
            if s and c:
                self.add_item(self.list_commands, c)
                self.options_dict[item.text()].append(c)
            else:
                self.show_msg('Warning!', 'You didn\'t enter the command!')
        self.update_label()

    def start_execute(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            command_list = [self.list_commands.item(i).text() for i in
                            range(self.list_commands.count())]
            if 'default' in [self.list_options.item(i).text() for i in
                             range(self.list_options.count())] and item.text() != 'default':
                command_list += [self.list_commands_default.item(i).text() for i in
                                 range(self.list_commands_default.count())]
            self.from_disable(True)
            self.my_exec.commands_pack = command_list
            self.my_exec.log_status = self.ch_log.isChecked()
            self.my_exec.pack_name = item.text()
            self.my_exec.start()

    def edit_command(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            commands_items = self.list_commands.selectedItems()
            if commands_items:
                command_item = commands_items[0]
                c, s = QInputDialog.getText(self, f'Rename {command_item}?',
                                            'Enter a new name for the package: ',
                                            text=f'{command_item.text()}')
                if c and s:
                    self.options_dict[item.text()].remove(command_item.text())
                    self.options_dict[item.text()].append(c)
                    self.list_commands.takeItem(self.list_commands.row(command_item))
                    self.add_item(self.list_commands, c)
        self.update_label()

    @staticmethod
    def add_item(obj, item: str) -> None:
        obj.addItem(item)

    def selectionChanged(self):
        items = self.list_options.selectedItems()
        if items:
            item = items[0]
            self.list_commands.clear()
            self.list_commands_default.clear()
            for command in self.options_dict[item.text()]:
                self.add_item(self.list_commands, command)
            if 'default' in self.options_dict and item.text() != 'default':
                for command in self.options_dict['default']:
                    self.add_item(self.list_commands_default, command)
        self.update_label()

    def at_start(self):
        self.from_disable(True)
        self.progress_bar.setValue(0)

    def at_finish(self) -> None:
        self.from_disable(False)
        self.progress_bar.setValue(100)
        self.show_msg(title='The program is completed',
                      msg=f'Completed commands: {len(self.my_exec.commands_pack)} '
                          f'| Errors: {len(self.my_exec.errors)}')
        self.my_exec.reset()

    def get_default_file(self):
        if os.path.exists('commandoro/default_pack.json'):
            self.open_file('commandoro/default_pack.json')
        elif os.path.exists('default_pack.json'):
            self.open_file('default_pack.json')

    def open_file(self, file_name):
        data: dict = open_json(file_name)
        if data:
            config_dict = make_dict(data)
            if config_dict:
                self.options_dict.clear()
                self.list_commands_default.clear()
                self.list_options.clear()
                self.list_commands.clear()
                self.options_file = file_name
                self.options_dict = config_dict
                self.print_console(f'Settings added successfully: {self.options_file}')
                for name in config_dict.keys():
                    self.add_item(self.list_options, name)
            else:
                self.print_console('Settings not found!')
        else:
            msg = f'Error in the configuration file: {file_name}'
            self.show_msg('Warning!', f'{msg}')
            self.print_console(msg)
        self.update_label()

    def from_disable(self, status: bool = False) -> None:
        self.btn_show_help.setDisabled(status)
        self.btn_console_clear.setDisabled(status)
        self.btn_open_file.setDisabled(status)
        self.btn_reset.setDisabled(status)
        self.btn_reset.setDisabled(status)
        self.btn_new_pack.setDisabled(status)
        self.btn_remove_pack.setDisabled(status)
        self.btn_edit_pack_name.setDisabled(status)
        self.btn_save.setDisabled(status)
        self.btn_save_as.setDisabled(status)
        # self.btn_del_file.setDisabled(status)
        self.btn_command_add.setDisabled(status)
        self.btn_command_edit.setDisabled(status)
        self.btn_exec.setDisabled(status)
        self.btn_command_remove.setDisabled(status)


def main():
    app = QApplication(sys.argv)
    form = MyWindow()
    form.resize(640, 480)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

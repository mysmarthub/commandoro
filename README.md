Commandoro
===
---
    Created: Aleksandr Suvorov
---
[![PyPI](https://img.shields.io/pypi/v/commandoro)](http://pypi.org/project/commandoro)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/commandoro)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/commandoro)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mysmarthub/commandoro)
![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/commandoro/total)
![PyPI - Downloads](https://img.shields.io/pypi/dm/commandoro)
![GitHub](https://img.shields.io/github/license/mysmarthub/commandoro)
![GitHub User's stars](https://img.shields.io/github/stars/mysmarthub?style=social)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/commandoro)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/mysmarthub/commandoro)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/commandoro)
>Utility for automatic command execution
---

Description
---

>With this utility, you can automate
the execution of commands on a Linux system.
Create a settings file with the necessary items,
in each item, collect the necessary commands,
and start their automatic execution when necessary.

>With this utility, it is very convenient 
to perform routine tasks , as well as configure 
and install the system after installation.

>The settings file is very simple and clear, 
and all the commands you need for different 
cases or different systems will be stored in one place.

>You can create your own files with settings 
or edit the default settings file, 
just specify the path to your file when running the script.

>After starting, the program will prompt you to 
select the desired item, and then execute all the 
commands that are stored in the file with the 
settings under this name.

---

Help:
----

```
usage: Commandoro [-h] [--v] [path]

Utility for automatic command execution

positional arguments:
  path            Path to the settings file

optional arguments:
  -h, --help      show this help message and exit
  --v, --version  Program version

The configuration file must be a file in the format .json and have the correct settings
```

---

Installation and launch:
---
    You can install the utility using pip, pipenv:

`pip install commandoro`

`pipenv install commandoro`

`sudo pip install commandoro`

`sudo pipenv install commandoro`

    And then run it like this:

`commandoro`

`commandoro /path to the settings file/config.json`

>On some systems, some commands require administrator rights, 
> so you can install the utility and run it further using:

`sudo pip install commandoro`

`sudo pipenv install commandoro`

`sudo commandoro`

`sudo commandoro /path to the settings file/config.json`

>You can download the source files and run using Python:

```
git clone https://github.com/mysmarthub/commandoro.git
python commandoro/commandoro/start.py
 
 or

sudo python commandoro/commandoro/start.py
```
---

Disclaimer
---

> Attention!
> Be very careful with the commands you pass to the program.
> The author of the program does not bear any responsibility for your actions, but
> provides only an automated shell for executing commands on your system.

---
[GitHub](https://github.com/mysmarthub/commandoro) / [PyPi](https://pypi.org/project/commandoro/)
---


>When creating your own files, use
the structure from the default file.

```json
{
  "Name to be displayed in the list of commands": [
    "command one",
    "command two"
  ],
  "Next name": [
    "command one",
    "command two"
  ]
}
```

info:
---
    Copyright © 2020 Aleksandr Suvorov
    Licensed under the terms of the MIT License
---

Support:
---
    Email: myhackband@yandex.ru
---

Help the project financially:
---
>Yandex Money:
https://money.yandex.ru/to/4100110928527458

>Sberbank Russia:
4276 4417 5763 7686

---
[![Download Commandoro](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/commandoro/files/latest/download)

---
[![Download Commandoro](https://img.shields.io/sourceforge/dt/commandoro.svg)](https://sourceforge.net/projects/commandoro/files/latest/download)
Commandoro
===
---

[Cli command manager] - Console command manager. My new project 


***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)
[![Donate](https://img.shields.io/static/v1?label=Python&message=3&color=yellow)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/commandoro)](http://pypi.org/project/commandoro)
[![Donate](https://img.shields.io/static/v1?label=donate&message=paypal&color=green)](https://paypal.me/myhackband)
[![Donate](https://img.shields.io/static/v1?label=donate&message=yandex&color=yellow)](https://yoomoney.ru/to/4100115206129186)

---

>Utility for automating command execution

    Author and developer: Aleksandr Suvorov

---

[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandoro)](http://pypi.org/project/commandoro)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/commandoro)](http://pypi.org/project/commandoro)
[![GitHub](https://img.shields.io/github/license/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/commandoro?style=social)](https://github.com/mysmarthub/commandoro)
[![GitHub watchers](https://img.shields.io/github/watchers/mysmarthub/commandoro?style=social)](https://github.com/mysmarthub/commandoro)
![GitHub forks](https://img.shields.io/github/forks/mysmarthub/commandoro?style=social)

---

[![Download Commandoro](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/commandoro/files/latest/download)
[![Download Commandoro](https://img.shields.io/sourceforge/dt/commandoro.svg)](https://sourceforge.net/projects/commandoro/files/latest/download)

---

[![Commandoro](https://github.com/mysmarthub/commandoro/raw/master/images/commandoro_logo.png)](https://github.com/mysmarthub/commandoro)
[![Commandoro](https://github.com/mysmarthub/commandoro/raw/master/images/commandoro_gui_logo.png)](https://github.com/mysmarthub/commandoro)

---


Help the project financially:
-----------------------------
 If you like my projects, you can support me financially.

> PayPal: https://paypal.me/myhackband

> Yandex money: https://yoomoney.ru/to/4100115206129186

> Visa: 4048 0250 0089 5923


> If you can't find a way to donate, write to me:
 mailto: `mysmarthub@ya.ru`


---
What's news?
---
1. Changed interface
2. An added menu for working with file. 
3. Removed -d option
4. Removed option -y
5. Added option -a
6. Added the ability to select autorun commands.
7. If you do not select autorun or do 
   not specify an option -a, the program will ask 
   for permission to execute commands, 
   which will allow unnecessary commands to be skipped.
   
8. If you do not select autorun, 
   after the program finishes, 
   you can return to the selection 
   of packages, or exit.
   
9. Dismissed the possibility of using the default package, 
   now the package named "default" 
   must be run as a regular package.

---
Termux support:
---------------
You can easily use the utility with Termux on mobile phones and tablets.

1. Install Termux

2. Run in termux:

`pkg install python`

`pip install commandoro --force`

`commandoro --help`

---


Description:
------------

The console version:
--------------------

> Commandoro - CLI utility for automatic command execution.

> The idea is to store different sets(packages) of commands in a
 single file, and run them automatically at any time.

> The program executes commands, the commands are stored in packages,
 and the packages are stored in a file.

> The program uses a file in json format with the structure:

```json
{
  "Name1": [
    "command one",
    "command two"
  ],
  "Name2": [
    "command one",
    "command two"
  ],
  "Name3": [
    "command one",
    "command two"
  ]
}

```
>where keys are package names and values are lists of commands.

> For convenience, you can create a package named "
default" and store common commands in it, which are the same in some packages.

> You can pass the file name as an argument when running -f [file path]
 or --file [file path].

> You can also specify the program name with -n or 
> the --name parameter, if you have a package with that name, 
> then the command package with this name will be selected, 
> if you specify the -а parameter, 
> the automatic execution of commands from this package will start. 
> This is necessary, for example, 
> in order to create tasks in the scheduler and automatically launch 
> the utility with the right command package at the right time, 
> without your participation.

> Attention! Some commands require you to run as an administrator.
   To run some commands,
   you need to install dependencies on admin name:

`sudo pip install -r requirements.txt`

> With this utility, you can easily automate
manual execution, storage, and automatic execution of commands.

> With this utility it is very convenient to automatically execute
   necessary commands and configure the system after installation.

> The settings file is very simple and straightforward,
and all the necessary commands for different
cases or different systems will be stored in one place.
You will not need to store them in memory,
in different files, or search the Internet every time.

> If you created your own command package file,
just give the full path to this file at startup: --file file.json
> 
> The file must be in json format and have the required structure.

---
Help:
----

```
Usage: commandoro.py [OPTIONS]

  Commandoro - CLI utility for automatic command execution.

  - Run the utility without parameters to manually select options.

  Example: commandoro python commandoro.py

  - Use the option -f/--file [filename] to select a file with command
  packages.

  Example: commandoro -f file.json python commandoro.py -f file.json

  - Use the option -n/--name to specify an existing package name.

  Example: commandoro -f file.json -n Ubuntu python commandoro.py -f
  file.json -n Ubuntu

  - Use the option -a for autorun and auto-completion.

  Example: commandoro -f file.json -n Ubuntu -a python commandoro.py -f
  file.json -n Ubuntu -a

  Author and developer: Aleksandr Suvorov

  Url: https://github.com/mysmarthub/

  Email: mysmarthub@ya.ru

  Donate: https://paypal.me/myhackband

  https://yoomoney.ru/to/4100115206129186

  4048 0250 0089 5923

Options:
  -f, --file FILE  The path to the file with the command packs
  -n, --name TEXT  Name of the package
  -a, --auto       Auto command execution, auto exit
  -v, --version    Displays the version of the program and exits.
  --help           Show this message and exit.

```

---

Installation and launch:
------------------------

> You can install the utility using pip:

`pip install commandoro`


`sudo pip install commandoro`

> And then run it like this:

`commandoro`

`commandoro --file config.json`

`commandoro --file config.json --name Ubuntu -a`

> On some systems, some commands require administrator rights,
 so you can install the utility and run it further using:

`sudo pip install commandoro`

`sudo commandoro`

`sudo commandoro --file config.json --name Ubuntu -a`

> You can download the source files and run using Python:

`wget https://github.com/mysmarthub/commandoro/archive/master.zip`

`git clone https://github.com/mysmarthub/commandoro.git`

`cd commandoro`

`pip install -r requirements`

`python commandoro.py --file commandoro/config.json`

or

`sudo pip install -r requirements`

`sudo python commandoro.py`

> If run without options, you will be prompted to select or create a file.
> 
> Если указать опцию -f [адрес файла] и передать ей адрес к файлу с пакетами комманд,
> будет пердложено выбрать нужный пакет.
> If you specify the -f [file address] option and pass 
> it the address to the file with command packages.
> 
> Specifying the -n [package name] option and specifying an existing package name will select that package.
> 
> If you specify the -a parameter, the program will auto-complete 
> if you specify the correct path to the file
> and the correct package name, the script will execute the commands 
> from the specified package automatically, with automatic completion.

---
Links:
------
> Github: https://github.com/mysmarthub/commandoro

> PyPi: https://pypi.org/project/commandoro/

> Sourceforge: https://sourceforge.net/projects/commandoro/files/latest/download

---

Disclaimer of liability:
------------------------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
Requirements:
---

Uses [Click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/master/LICENSE.rst)

[Python 3+](https://python.org)

---
Support:
---
    Email: mysmarthub@ya.ru
    Copyright © 2020-2021 Aleksandr Suvorov

-----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
-----------------------------------------------------------------------------

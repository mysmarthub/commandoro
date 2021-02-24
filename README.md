Commandoro
===
---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)
[![Donate](https://img.shields.io/static/v1?label=Python&message=3&color=yellow)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/commandoro)](http://pypi.org/project/commandoro)
[![Donate](https://img.shields.io/static/v1?label=donate&message=paypal&color=green)](https://paypal.me/myhackband)
[![Donate](https://img.shields.io/static/v1?label=donate&message=yandex&color=yellow)](https://yoomoney.ru/to/4100115206129186)

---

>Console and graphical utility for automating command execution

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
 If you like my projects, you can support me financially -
 " for an apartment in Moscow or a hut in the taiga) ..."

> PayPal: https://paypal.me/myhackband

> Yandex money: https://yoomoney.ru/to/4100115206129186

> Visa: 4048 0250 0089 5923


> If you can't find a way to donate, write to me:
 mailto: `mysmarthub@ya.ru`

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
  "Commands pack name": [
    "command one",
    "command two"
  ],
  "Next commands pack name": [
    "command one",
    "command two"
  ],
  "default": [
    "command one",
    "command two"
  ]
}

```
>where keys are package names and values are lists of commands.

> For convenience, you can create a package named "
default" and store common commands in it, which are the same in some packages.

> Use the -d option when starting the utility
 to execute commands from the "default" package
 after executing the main package of your choice.

> You can pass the file name as an argument when running -f [file path]
 or --file [file path].

> You can also specify the name of the program using the -n or
 --name parameter, if you have a package with this name,
 the automatic execution of commands from this package will begin.
 This is necessary in order to, for example,
 create tasks in the scheduler and automatically run
 the utility with a batch of commands at the right time,
 without your participation.

> Attention! Some commands require you to run as an administrator.
 To run some commands in graphical mode,
 you need to install dependencies on the administrator name:

`sudo pip install -r requirements.txt`

> With this utility, you can easily automate
manual execution, storage, and automatic execution of commands.

> Create your own file with command packages or use and
edit the default file. In the settings file, create
new command packages, use the key as the package name
and the value as the list of commands (see the default file).

> With this utility, it is very convenient
 to perform routine tasks, automatically execute the
 necessary commands, and configure the system after installation.



> The settings file is very simple and clear,
and all the commands you need for different
cases or different systems will be stored in one place.
You will not need to keep them in memory,
in different files, enter them manually or search the Internet.

> There is a "default" section in the settings file, from which commands
will be executed in any case.
This is done to combine common commands
for all command packages into a single default package.

> If you have created your own settings file,
just specify the full path to this file when
running the script as a parameter -f [config.json] or --file [config.json].
 If you are using the graphical version of the program,
just open the file with the settings using the open button.
The file must be in json format and have the required structure.

> After starting, the program will prompt you
to select the desired item, and then execute all
the commands that are stored in
the settings file under this name/key.

    Use -n [Command name] or --name [Command name] for automatic
    executing a batch of commands.

---
The GUI version:
----------------

> Graphical utility for automating the execution of command packages,
their creation, storage, editing, and launch.

> The graphical version allows you to open files with
command packages, change, add, delete packages,
save changes to a file, save all changes to a new file,
view commands from each package, change, add and delete commands.

> Execute commands without saving to a file,
edit packages and commands without saving,
add, remove, and modify the default package and commands from this package.
It has the function of recording work in a log file.


---
Help:
----

```
Usage: commandoro.py [OPTIONS]

  Commandoro - CLI utility for automatic command execution.

  - To work, it uses files that store named command packages,     where
  the name is the name of the command package,     and the value is a
  list of commands.

  - You can create your own files with command packages using the
  default structure, and pass the path to them as an argument at startup
  and pass the path to them as an argument at startup.

  - Use the name - "default" - name for the package with the default
  commands. You can perform them in addition to the selected command
  package.

  Author and developer: Aleksandr Suvorov

  Url: https://github.com/mysmarthub/

  Email: mysmarthub@ya.ru

  Donate: https://paypal.me/myhackband

  https://yoomoney.ru/to/4100115206129186

  4048 0250 0089 5923

Options:
  -f, --file FILE  The path to the file with the command packs
  -d, --default    Run an additional batch of commands from default
  -n, --name TEXT  Name of the package
  -v, --version    Displays the version of the program and exits.
  -y, --yes        Auto command execution
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

`commandoro --file config.json --name Ubuntu -d -y`

> On some systems, some commands require administrator rights,
 so you can install the utility and run it further using:

`sudo pip install commandoro`

`sudo commandoro`

`sudo commandoro --file config.json --name Ubuntu -d -y`

> You can download the source files and run using Python:

`wget https://github.com/mysmarthub/commandoro/archive/master.zip`

`git clone https://github.com/mysmarthub/commandoro.git`

`cd commandoro`

`pip install -r requirements`

`python commandoro.py --file commandoro/config.json`

or

`sudo pip install -r requirements`

`sudo python commandoro.py`

    Commandoro Gui:
    ---------------

    pip install -r requirements.txt
    
    python commandoro_gui.py

    Sudo Commandoro Gui:
    --------------------

    sudo pip install -r requirements.txt
    sudo python commandoro_gui.py

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
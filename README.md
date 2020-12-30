Commandoro
===

>Console and graphical utility for automating command execution.

    Created: Aleksandr Suvorov
---
[![PyPI](https://img.shields.io/pypi/v/commandoro)](http://pypi.org/project/commandoro)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/commandoro)](http://pypi.org/project/commandoro)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandoro)](http://pypi.org/project/commandoro)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/commandoro)](http://pypi.org/project/commandoro)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/commandoro/total)](https://github.com/mysmarthub/commandoro)
[![GitHub](https://img.shields.io/github/license/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/commandoro?style=social)](https://github.com/mysmarthub/commandoro)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/mysmarthub/commandoro)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/commandoro)](https://github.com/mysmarthub/commandoro)

---
[![Download Commandoro](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/commandoro/files/latest/download)
[![Download Commandoro](https://img.shields.io/sourceforge/dt/commandoro.svg)](https://sourceforge.net/projects/commandoro/files/latest/download)
---

The console version:
---
![Commandoro console version](https://github.com/mysmarthub/commandoro/raw/master/images/commandoro.png)

>The console version allows you to run a script in the terminal, 
passing it a file with settings as an argument, 
or use the default file. In the process, you select the desired 
command package, then you can start execution, 
display a list of commands for this package, 
or return to the selection of the command package. 
After executing all the commands, 
the program goes to the main menu and again waits for 
input to select the desired package, or exit the program.
> 
> During execution, it displays information about the 
command number, the command itself, and the status 
of its execution. Upon completion, 
it displays information about the number of executed commands, 
and the number of errors during execution.

---
The GUI version:
---
![Commandoro gui version](https://github.com/mysmarthub/commandoro/raw/master/images/commandoro_gui.png)


>The graphical version allows you to open files with 
command packages, change, add, delete packages, 
save changes to a file, save all changes to a new file, 
view commands from each package, change, add and delete commands. 
Execute commands without saving to a file, 
edit packages and commands without saving, 
add, remove, and modify the default package and commands from this package. 
It has the function of recording work in a log file.


---

Help the project financially:
---
>Yandex Money:
https://yoomoney.ru/to/4100115206129186

    Visa:    4048 4150 0400 5852

    Sberbank Russia: 4276 4417 5763 7686

https://paypal.me/myhackband

---

Description
---

>Console and graphical versions are available.

>With this utility, you can automate
the execution of commands on a Linux system.
Create a file with command packages or use and 
edit the default file. In the settings file, create 
new command packages, use the key as the package name, 
and the value as the list of commands (see the default file).

>In each item, collect the necessary commands,
and start their automatic execution when necessary.

>With this utility, it is very convenient 
to perform routine tasks, automatically execute the necessary commands, 
and also configure the system after installation.

>The settings file is very simple and clear, 
and all the commands you need for different 
cases or different systems will be stored in one place.
You will not need to keep them in memory, 
in different files, enter them manually or search the Internet.

>In the settings file, there is a section from which commands 
will be executed in any case. 
This is done in order to bring common commands 
for all command packages into a single default package.

>You can create your own files with settings
or edit the default settings file. 
If you have created your own settings file, 
just specify the full path to this file when 
running the script as a parameter. 
If you are using the graphical version of the program, 
just open the file with the settings using the open button.
The file must be in json format and have the required structure.

>The section with the "default" commands will run anyway.

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

>After starting, the program will prompt you to 
select the desired item, and then execute all the 
commands that are stored in the file with the 
settings under this name/key.

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
    
    python commandoro/commandoro/commandoro.py
     
     or
    
    sudo python commandoro/commandoro/commandoro.py
    
    Commandoro Gui:
    ---------------
    
    pip install -r commandoro/requirements.txt 
    python commandoro/commandoro_gui.py
    
    Sudo Commandoro Gui:
    --------------------
    
    sudo pip install -r commandoro/requirements.txt 
    sudo python commandoro/commandoro_gui.py

```

>When creating your own files, use
the structure from the default file.

```json
{
  "Commands pack name": [
    "command one",
    "command two"
  ],
  "Next commands pack name": [
    "command one",
    "command two"
  ]
}
```
---

Links:
---
>[GitHub](https://github.com/mysmarthub/commandoro)
> 
>[PyPi](https://pypi.org/project/commandoro/)
> 
>[Sourceforge](https://sourceforge.net/projects/commandoro/files/latest/download)
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

Support:
---
    Email: myhackband@yandex.ru
    Copyright © 2020 Aleksandr Suvorov

Commandoro
===

    Utility for automatic command execution

>Created: Aleksandr Suvorov
---
[![PyPI](https://img.shields.io/pypi/v/commandoro)](http://pypi.org/project/commandoro)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/commandoro)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/commandoro)
![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/commandoro/total)
![PyPI - Downloads](https://img.shields.io/pypi/dm/commandoro)
![GitHub](https://img.shields.io/github/license/mysmarthub/commandoro)
![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/commandoro?style=social)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/commandoro)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/mysmarthub/commandoro)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/commandoro)

---
[![Download Commandoro](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/commandoro/files/latest/download)
[![Download Commandoro](https://img.shields.io/sourceforge/dt/commandoro.svg)](https://sourceforge.net/projects/commandoro/files/latest/download)
---

![Commandoro](https://github.com/mysmarthub/commandoro/raw/master/images/logo.png)

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

>With this utility, you can automate
the execution of commands on a Linux system.
Create a settings file with the necessary items,
or use/edit the default file.
In each item, collect the necessary commands,
and start their automatic execution when necessary.

>With this utility, it is very convenient 
to perform routine tasks , as well as configure 
and install the system after installation.

>The settings file is very simple and clear, 
and all the commands you need for different 
cases or different systems will be stored in one place.

>In the settings file, a section with a special 
name default is available, 
any commands added to this section 
will be executed by default after the 
main commands are executed.

>You can create your own files with settings
or edit the default settings file. 
If you have created your own settings file, 
just specify the full path to this file when 
running the script as a parameter. 
Keep in mind that at the moment the file 
must be in json format, have this file extension, 
and use the required structure:

>The section with the "default" commands will run anyway.

```json
{
  "Name to be displayed in the list of commands": [
    "command one",
    "command two"
  ],
  "Next name": [
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
python commandoro/commandoro/start.py
 
 or

sudo python commandoro/commandoro/start.py
```

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

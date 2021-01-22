Commandoro
==========

Console and graphical utility for automating command execution

Author and developer: Aleksandr Suvorov

---

Help the project financially:
-----------------------------
 If you like my projects, you can support me financially -
 " for an apartment in Moscow or a hut in the taiga) ..."

https://paypal.me/myhackband

Yandex money:

https://yoomoney.ru/to/4100115206129186

    Visa: 4048-4150-0400-5852



If you can't find a way to donate, write to me:
 mailto: mysmarthub@ya.ru

---


Termux support:
---------------
You can easily use the utility with Termux on mobile phones and tablets.

1. Install Termux
2. `pkg install python`
3. `pip install commandoro`
4. `commandoro --help`

---


Description:
------------

The console version:
--------------------

Commandoro - CLI utility for automatic command execution.

 The idea is to store different sets(packages) of commands in a
 single file, and run them automatically at any time.

 The program executes commands, the commands are stored in packages,
 and the packages are stored in a file.

 The program uses a file in json format with the structure:
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
 where keys are package names and values are lists of commands.

 For convenience, you can create a package named "
default" and store common commands in it, which are the same in some packages.

 Use the -d option when starting the utility
 to execute commands from the "default" package
 after executing the main package of your choice.

You can pass the file name as an argument when running -f [file path]
 or --file [file path], or use the default file, it should be
in the same directory as the file being run and called "config.json".


---

The GUI version:
----------------

Graphical utility for automating the execution of command packages,
their creation, storage, editing, and launch.

The graphical version allows you to open files with
command packages, change, add, delete packages,
save changes to a file, save all changes to a new file,
view commands from each package, change, add and delete commands.
Execute commands without saving to a file,
edit packages and commands without saving,
add, remove, and modify the default package and commands from this package.
It has the function of recording work in a log file.

---

 You can also specify the name of the program using the -n or
 --name parameter, if you have a package with this name,
 the automatic execution of commands from this package will begin.
 This is necessary in order to, for example,
 create tasks in the scheduler and automatically run
 the utility with a batch of commands at the right time,
 without your participation.

 Attention! Some commands require you to run as an administrator.
 To run some commands in graphical mode,
 you need to install dependencies on the administrator name:

    sudo pip install -r commandoro/requirements.txt

 With this utility, you can easily automate
manual execution, storage, and automatic execution of commands.

 Create your own file with command packages or use and
edit the default file. In the settings file, create
new command packages, use the key as the package name
and the value as the list of commands (see the default file).

 With this utility, it is very convenient
 to perform routine tasks, automatically execute the
 necessary commands, and configure the system after installation.



 The settings file is very simple and clear,
and all the commands you need for different
cases or different systems will be stored in one place.
You will not need to keep them in memory,
in different files, enter them manually or search the Internet.

 There is a "default" section in the settings file, from which commands
will be executed in any case.
This is done to combine common commands
for all command packages into a single default package.

 If you have created your own settings file,
just specify the full path to this file when
running the script as a parameter -f [config.json] or --file [config.json].
 If you are using the graphical version of the program,
just open the file with the settings using the open button.
The file must be in json format and have the required structure.

After starting, the program will prompt you
to select the desired item, and then execute all
the commands that are stored in
the settings file under this name/key.

 Use -n [Command name] or --name [Command name] for automatic
  executing a batch of commands.

---

Help:
----

```
Usage: commandoro.py [OPTIONS]

    Commandoro - CLI utility for automatic command execution

    - To work, it uses files that store named command packages,     where the
    name is the name of the command package,     and the value is a list of
    commands.

        You can create your own files with command packages using         the
        default structure.

    - Use the default name for the package with the default commands.     You
    can perform them in addition to the selected command package.

    - You can pass the file name as an argument,     or use the default file,
    it should be located     in the same directory as the file being run.

    -The console version allows you to run a script in the terminal,
    passing it a file with settings as an argument,     or use the default
    file. In the process, you select the desired     command package, then you
    can start execution,     display a list of commands for this package,
    or return to the selection of the command package.

    - After executing all the commands,     the program goes to the main menu
    and again waits for     input to select the desired package, or exit the
    program.

    - You can pass the name of the desired package,     and if it exists
    inside the file with the command settings from it     will be executed.

    - The examples run:

    python commandoro.py --file=config.json -d

    python commandoro.py --file=config.json -d --name=Ubuntu

  Options:
    -f, --file TEXT  The path to the file with the command packs
    -d, --default    Run an additional batch of commands from default
    -t, --test       Test run, commands will not be executed.
    -n, --name TEXT  Name of the package to run automatically
    --help           Show this message and exit.

```

---

Installation and launch:
------------------------

    You can install the utility using pip:

`pip install commandoro`


`sudo pip install commandoro`

    And then run it like this:

`commandoro`

`commandoro --file config.json -d`

`commandoro --file=config.json --name=Ubuntu -d`

On some systems, some commands require administrator rights,
 so you can install the utility and run it further using:

`sudo pip install commandoro`

`sudo commandoro --file=config.json --name=Ubuntu -d`

You can download the source files and run using Python:

`git clone https://github.com/mysmarthub/commandoro.git`

`cd commandoro`

`pip install -r requirements`

`python commandoro/commandoro.py --file=commandoro/config.json`

or

`sudo pip install -r requirements`

`sudo python commandoro/commandoro/commandoro.py`

    Commandoro Gui:
    ---------------

    pip install -r commandoro/requirements.txt
    python commandoro_gui.py

    Sudo Commandoro Gui:
    --------------------

    sudo pip install -r requirements.txt
    sudo python commandoro_gui.py

---

Links:
------
https://github.com/mysmarthub/commandoro

https://pypi.org/project/commandoro/

https://sourceforge.net/projects/commandoro/files/latest/download

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

    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------

Uses Click
https://github.com/pallets/click

 by license:

 https://github.com/pallets/click/blob/master/LICENSE.rst

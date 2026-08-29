# AUTOWRITE
# _______________

# This program is to write a text with a typewriter effect.
# OTHER FEATURES:

# DELAY/ VELOCITY:
# Time slack between a letter and the other.
# You can change it by writing "delay", then you will see the 
# text "change the single letter split's delay to". Then write a number (better if its between 0.2 and 0.30).

# REPEAT:
# Repeat the text you wrote.


# set delay and define error exit func.
delay = 0.10
count = 1

def exit_error():
    config.exit(1)

# for some misterious motivations, it now works.
# remember: NEVER EDIT THIS UNLESS YOU REALLY NEED TO DO THAT.

# who knows.

def repeat():
    global count
    global repl

    print("how much times you want the text is repeated?")
    try:
        count = input()
    except ValueError:
        print("insret a number.")
        config.exit(1)
    repl = "setting updated with success!"

#the following lines was putted in another place of the file
#but it was:

# repl = str(repl * (int(count)))


# and to change the text input:

def set_delay():
    global delay

    print("change the single letter split's delay to")
    try:
        delay = float(input())
    except ValueError:
        print("insret a number.")
        config.exit(1)

    global repl
    repl = "delay changed with success!"
    print()

# other commented way: clears the text input

#    global repl
#    repl = " "
#    print()

#is the module imported correctly?

from pathlib import Path as pth

# WARNING WARNING!!!:
# **The following worning i sold, the code its about is already fixed and added!**

# WARNING: the font import is a bit poorly programmed: trying to import. Arial couldn't work.
# Is this feature in progress.

# Commented definitions blocks are diabled because fonts are into folders.
# the path could be redirected by writing C:\Windows\Fonts\fntfolder\normalfont

# That will be added soon.

def importArial():
    font = pth("C:\Windows\Fonts\Arial\Arial Normale")

def importCalibri():
    font = pth("C:\Windows\Fonts\Calibri\Calibri Normale")

def importGeorgia():
    font = pth("C:\Windows\Fonts\Georgia\Georgia Normale")

def importVerdana():
    font = pth("C:\Windows\Fonts\Verdana\Verdana Normale")

def importTahoma():
    font = pth("C:\Windows\Fonts\Tahoma\Tahoma Normale")

def importTimesNewRoman():
    font = pth("C:\Windows\Fonts\Times New Roman\Times New Romane Normale")

def importCourierNew():
    font = pth("C:\Windows\Fonts\Courier New\Courier New Normale")

# the following 2 paths is for a font is ALREADY the normal font:

def importLucidaConsole():
    font = pth("C:\Windows\Fonts\Lucida Console Normale")

def importFixedSys():
    font = pth("C:\Windows\Fonts\FixedSys Normale")


# WARNING: the font import is a bit poorly programmed: trying to import
# some fonts can return errors. For example, Times New Roman doesn't works, so is commented:

#def importTimesNewRoman():
#    font = pth("C:\Windows\Fonts\Times New Roman")

try:
  import sys as config
except ImportError:
  print("error: module import fail")
  exit_error()
except ModuleNotFoundError:
  print("error: module not imported")
  exit_error()

# normally, these 2 modules shouldn't return the second error (ModuleNotFoundError)
# but the first error, ImportError, could happen.

try:
  import time
except ImportError:
    print("error: module import fail")
    exit_error()
except ModuleNotFoundError:
    print("error: module not imported")
    exit_error()
    
# remember: NEVER edit the following part of the file. Terrible bugs could happen.
# really. Don't do that. Pls persor of the future, DONT DO THAT!!!!
# (unless you have to fix a bug)
# all good, let's write:

while True:
    print("witch text you want to automate?")
    repl = input()

    if repl == "exit":
        config.exit(0)

    if repl == "delay":
        set_delay()

    if repl == "repeat":
        repeat()

    
    repl = (str(repl) * (int(count))) 

    for digit in repl:

        print(digit, end="")
        config.stdout.flush()
    
        time.sleep(delay)

    print()

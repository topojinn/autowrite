# AUTOWRITE
# _______________

# LINKS:
# official GitHub rpository | https://github.com/topojinn/autowrite/
# official License text | https://github.com/topojinn/autowrite/blob/main/LICENSE/
# online code backup | https://github.com/topojinn/autowrite/blob/main/main.py/

# !!online code backup advice!! :
# NOT ALWAYS UPDATED.
# Every day the code is being updated, but not always published.

# for example, at this time, youre pribably reading an non-updated text file.

# OTHER:

# This program is to write a text with a typewriter effect.
# FEATURES / EXTRA FEATURES:

# DELAY/ VELOCITY:
# Time slack between a letter and the other.
# You can change it by writing "delay", then you will see the 
# text "change the single letter split's delay to". Then write a number (better if its between 0.2 and 0.30).

# REPEAT:
# Repeat the text you wrote for a value.

# FONT:
# Change the font of the typewriter.
# - supported fonts:

#* Arial - https://learn.microsoft.com/en-us/typography/font-list/arial
#* Calibri - https://learn.microsoft.com/en-us/typography/font-list/calibri
#* Georgia - https://learn.microsoft.com/en-us/typography/font-list/georgia
#* Verdana - https://learn.microsoft.com/en-us/typography/font-list/verdana
#* Tahoma - https://learn.microsoft.com/en-us/typography/font-list/tahoma
#* Times New Roman - https://learn.microsoft.com/en-us/typography/font-list/times-new-roman
#* Courier New - https://learn.microsoft.com/en-us/typography/font-list/courier-new
#* Lucida Console - https://learn.microsoft.com/en-us/typography/font-list/lucida-console
#* FixedSys - https://en.wikipedia.org/wiki/Fixedsys

# !FONT FEATURE WARNING!
# The path used to import these fonts is based on Italian system.
# For another windows system not configured as Italian, this feature shouldn't work.

# This will be fixed soon.

# GENERAL > ACTUAL BUGS:
# In general, the font feature doesn't work, but this isn't considerable as a bug, Is only a W.I.P. feature.

#general bugs count:
# bugs known: 0 | features bugged/WIP: 1

# CREDITS:
# Written by topojinn | https://github.com/topojinn/
# Code Review by egipros06 | https://egipros06.newgrounds.com/
# Language: Python | https://www.python.org/ or https://github.com/python/

# Written IN VScode | https://code.visualstudio.com/ or https://github.com/microsoft/vscode/


# LICENSE:
# MIT License

# Copyright (c) 2026 topojinn

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

def selectFont():
    global repl
    global fontName

    repl = "change actual font to:"
    fontName = input()

    if fontName == "Arial": #C:\Windows\Fonts\Arial\Arial Normale
        importArial()

    if fontName == "Calibri": #C:\Windows\Fonts\Calibri\Calibri Normale
        importCalibri()

    if fontName == "Georgia": #C:\Windows\Fonts\Georgia\Georgia Normale
        importGeorgia()

    if fontName == "Verdana": #C:\Windows\Fonts\Verdana\Verdana Normale
        importVerdana()

    if fontName == "Tahoma": #C:\Windows\Fonts\Tahoma\Tahoma Normale
        importTahoma()

    if fontName == "Times New Roman": #C:\Windows\Fonts\Times New Roman\Times New Romane Normale
        importTimesNewRoman()

    if fontName == "Courier New": #C:\Windows\Fonts\Courier New\Courier New Normale
        importCourierNew()

    if fontName == "Lucida Console": #C:\Windows\Fonts\Lucida Console Normale
        importLucidaConsole()

    if fontName == "FixedSys": #C:\Windows\Fonts\FixedSys Normale
        importFixedSys()


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

    if repl == "font":
        selectFont()


    
    repl = (str(repl) * (int(count))) 

    for digit in repl:

        print(digit, end="")
        config.stdout.flush()
    
        time.sleep(delay)

    print()

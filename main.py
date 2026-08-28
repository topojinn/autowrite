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
    count = input()

#the following lines was putted in another place of the file
#but it was:

# repl = str(repl * (int(count)))


# and to change the text input:

def set_delay():
    global delay

    print("change the single letter split's delay to")
    delay = float(input())

    global repl
    repl = "delay successfully resetted"
    print()

# other commented way: clears the text input

#    global repl
#    repl = " "
#    print()

#is the module imported correctly?
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

# all good, let's write:

while True:
    print("witch text you want to automate?")
    repl = input()

    if repl == "exit":
        config.exit(0)

    elif repl == "delay":
        set_delay()

    elif repl == "repeat":
        repeat()

    
    repl = (str(repl) * (int(count)))

    try:
        for digit in repl:

            print(digit, end="")
            config.stdout.flush()
    
            time.sleep(delay)
            print()

    except:
        print("sorry, there was an unknown error. ")

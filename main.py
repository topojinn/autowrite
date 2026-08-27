# set delay and define error exit func.
delay = 0.10

def exit_error():
    config.exit(1)

# for some misterious motivations, it now works.
# probably for the global function or maybe the float input.

# who knows.

def set_delay():
    global delay

    print("change the single letter split's delay to")
    delay = float(input())                                        

# chang the text input
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

    if repl == "delay":
        set_delay()

    for digit in repl:

        print(digit, end="")
        config.stdout.flush()
    
        time.sleep(delay)

    print()

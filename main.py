#set delay and define error exit func.
delay = 0.10

def exit_error():
    config.exit(1)

# (all this block should work, or shouldnt work.)
# (i think is randomized.)
# (i'm not sure how.)

def set_delay():
    print("change the single letter split's delay to")
    delay = input()                                        

    print()
    repl = "delay changed with success"

#is the module imported correctly?
try:
  import sys as config
except ImportError:
  print("error: module import fail")
  exit_error()
except ModuleNotFoundError:
  print("error: module not imported")
  exit_error()


try:
  import time
except ImportError:
    print("error: module import fail")
    exit_error()
except ModuleNotFoundError:
    print("error: module not imported")
    exit_error()

#all good, let's write:

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

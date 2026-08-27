#set delay
delay = 0.10

def exit_error():
    config.exit(1)

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


print("with text you want to automate?")
repl = input()

if repl == "exit":
  config.exit(0)

for digit in repl:

    print(digit, end="")
    config.stdout.flush()
    
    time.sleep(delay)

print()

try:
  import sys as config
except ImportError:
  print("error: module import fail")
except ModuleNotFoundError:
  print("error: module not imported")

try:
  import time
except ImportError:
    print("error: module import fail")
except ModuleNotFoundError:
    print("error: module not imported")

print("with text you want to automate?")
repl = input()

if repl == "exit":
  config.exit(0)

for digit in repl:

    print(digit, end="")
    config.stdout.flush()
    
    time.sleep(0.05)

print()

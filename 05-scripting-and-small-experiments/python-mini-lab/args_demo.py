import sys

for index, argument in enumerate(sys.argv):
    print(f"argv[{index}] = {argument!r}")
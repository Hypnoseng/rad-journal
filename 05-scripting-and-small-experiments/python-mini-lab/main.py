from utils import greet,add
import os
import sys

print(greet("Python"))
print(add(10,20))

print("CWD:", os.getcwd())
print("sys.path[0]:", repr(sys.path[0]))
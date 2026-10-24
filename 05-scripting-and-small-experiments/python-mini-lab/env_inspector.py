import sys
import json

print("=== Python Environment Inspector ===")
print(f"Executable   : {sys.executable}")
print(f"Prefix       : {sys.prefix}")
print(f"Base prefix  : {sys.base_prefix}")
print(f"Python version: {sys.version}")
print(f"Is venv      : {sys.prefix != sys.base_prefix}")


print("\n=== Module Search Path ===")

for path in sys.path:
    print(path)

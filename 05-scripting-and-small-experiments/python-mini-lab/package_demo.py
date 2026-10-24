import sys

import myutils.math_tools

print("Package cached:", "myutils" in sys.modules)
print("Module cached:", "myutils.math_tools" in sys.modules)
print("Module object:", sys.modules["myutils.math_tools"])
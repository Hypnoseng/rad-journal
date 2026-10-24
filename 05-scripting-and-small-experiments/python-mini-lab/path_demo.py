from pathlib import Path

# Current working directory
cwd = Path.cwd()
print("Current directory:", cwd)

# Path to this script
script_path = Path(__file__)
print("Script path:", script_path)

# Script's parent directory
project_dir = script_path.parent
print("Project directory:", project_dir)

# Check whether paths exist
print("Project exists:", project_dir.exists())
print("Is directory:", project_dir.is_dir())

# List Python files in the project directory
print("Python files:")
for path in sorted(project_dir.glob("*.py")):
    print(" -", path.name)


from pathlib import Path

relative_path = Path("greet.py")
absolute_path = relative_path.resolve()

print("Relative path:", relative_path)
print("Absolute path:", absolute_path)
print("Relative exists:", relative_path.exists())
print("Absolute exists:", absolute_path.exists())

relative_path = Path("greet.py")
print(relative_path.exists())
script_dir = Path(__file__).resolve().parent
greet_path = script_dir / "greet.py"

print(greet_path)
print(greet_path.exists())
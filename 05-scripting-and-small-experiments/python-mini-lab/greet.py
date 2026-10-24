
import argparse

parser = argparse.ArgumentParser(
    description="Greet someone."
)

parser.add_argument(
    "--name",
    default="Python",
    help="Name to greet"
)

args = parser.parse_args()

print(f"Hello, {args.name}!")

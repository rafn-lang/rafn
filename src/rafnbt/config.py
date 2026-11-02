import sys
import tomllib
from pathlib import Path


def has_config():
    return Path("rafn.toml").is_file()


def get_config():
    if not has_config():
        print("Not in a Rafn project: No rafn.toml found")
        sys.exit(1)

    with open("rafn.toml", "rb") as f:
        data = tomllib.load(f)

    return data

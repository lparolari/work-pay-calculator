from boot import boot
from wpc.cli import cli

if __name__ == "__main__":
    boot.bootstrap()
    cli.cli_commands()

# this script can be used in IDE (PyCharm) as script path.
# the shell entry point is defined in setup.py.

import pathlib

# Read version from VERSION file
HERE = pathlib.Path(__file__).parent
__version__ = (HERE.parent / "VERSION").read_text().strip()

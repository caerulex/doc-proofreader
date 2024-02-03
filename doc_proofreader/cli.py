# Copyright caerulex 2024

"""CLI setup."""

import argparse

parser = argparse.ArgumentParser(
    prog="Doc-Proofreader",
    description="Proofreads documents with AI!",
    epilog="A simple app by caerulex.",
)
parser.add_argument("file_path", metavar="file-path")
parser.add_argument("--additional-instructions", type=str, default="")

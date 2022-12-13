import argparse
import datetime
from pathlib import Path

parser =argparse.ArgumentParser(descriptionprog="ls",
 description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    )

target_dir=[]
build_output=()  
for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))

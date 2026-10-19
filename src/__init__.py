from os import walk
from os.path import join
from pathlib import Path
from shutil import rmtree

for i, j, _ in walk(Path(__file__).parent):
    for k in j:
        if k.find("__pycache__") >= 0:
            rmtree(join(i, k))

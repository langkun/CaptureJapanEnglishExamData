import shutil
from pathlib import Path
import os

def createFolder(folder_name):
    if not Path(folder_name).exists():
        os.makedirs(folder_name)

def move(folder_name):
    createFolder(folder_name)
    for f in Path().resolve().iterdir():
        if( f.is_file() and (f.name.endswith('.pdf') or f.name.endswith("mp3"))):
            shutil.move(f.name, Path(folder_name))
                       
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "CNN_Classifier"

list_of_files = [
    '.github/wokflows/.gitkeep',
    f"src/{project_name}/__init__.py", #init is called a constructor file and it can be used to import functions from a different folder kinda
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utilities/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "parameters.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok = True) #exist arg checks if we already have a dir or not, and if we have it, it doesn't create a new one.
        logging.info(f"creating directory: {filedir} for the file: {filename}")
        
    if (os.path.exists(filepath) == False) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
    

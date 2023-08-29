# Compulsory this library or code import all project
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlproject" # this name mention as your wish don't required any where its just for this module project package 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # this code have new additions
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",# this code have new additions
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    # "dvc.yaml", # this file not required because we can use ML FLOWS
    "params.yaml",
    "schema.yml", # this code have new additions
    "main.py", # this code have new additions, but this file you have created manually project
    "app.py", # this code have new additions, but this file you have created manually project
    "Dockerfile", # this code have new additions, but this file you have created manually project
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    # Sometimes getting a issue for backslashes because normally computer use the forward slashes so that above file use / forward slashes, below code help
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
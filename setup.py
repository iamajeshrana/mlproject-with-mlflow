# Compulsory this code used in  all project
# Why used setup.py because src/mlproject/components/ as a totally localpackage that package i can use evry where where required.

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "mlproject-with-mlflow" # This name gives as per given the project repo name in github
AUTHOR_USER_NAME = "iamajeshrana"
SRC_REPO = "mlproject" # this names gives as per the mention the src/mlproject name
AUTHOR_EMAIL = "iamajeshrana4u@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app", # If you ML project create then type ML, if you have DL project then type DL
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
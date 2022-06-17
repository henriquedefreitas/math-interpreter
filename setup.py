from os import path
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name='compiler',
    long_description=readme,
    packages=find_packages(where="."),
)
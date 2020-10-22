from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='database_interaction',
    author="Alexander Gusarin",
    author_email="algu.remail@gmail.com",
    description="Classes to ease interaction with databases.",
    version='0.0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    python_requires='>=3.6',
)

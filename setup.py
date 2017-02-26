# setup.py
from setuptools import setup, find_packages

import simplepath

setup(
    name='simplepath',
    version=simplepath.__version__,
    packages=find_packages(),
    author="Quentin Chenevier",
    author_email="",
    description="Helping working with complex directory arborescences",
    long_description=open('README.md').read(),
    # install_requires= ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"],
    include_package_data=True,
    url='http://github.com/quent1chenevier/simplepath',

    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
    ],

    license="WTFPL",
)

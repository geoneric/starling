#!/usr/bin/env python
import codecs
import os
import setuptools
import sys


__version__ = "0.0.5"


here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file
with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()


setuptools.setup(
    name="starling",
    version=__version__,
    description="The Starling Python package contains code that might be "
        "useful when implementing services in Python",
    long_description=long_description,
    author="Kor de Jong",
    author_email="k.dejong@geoneric.eu",
    url="https://github.com/geoneric/starling",
    packages=setuptools.find_packages(),  # "source"),
    # package_dir={"": "source"},
    install_requires=[
        "flask>=0.11",
        "tzlocal>=1.3",
    ],
    license="MIT License",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Starling, microservice, service, Flask",
    zip_safe=True,
)

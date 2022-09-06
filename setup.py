#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Pycdek",
    version="0.1.0",
    description="Asynchronous python implementation of CDEK API v2.0",
    author="Andrey Volobuev",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pycdek"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["pydantic", "aiohttp"],
    python_requires=">=3.10",
    extras_require={
        "testing": ["unittest"],
    },
    include_package_data=True,
)

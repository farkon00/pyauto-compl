#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setuptools.setup(
        name="pyauto-compl", 
        version="0.1", 
        author="farkon00",
        author_email="sammer2016sammer@gmail.com",
        description="Library for auto complete in Python. It comes with set of standard english words for quick start.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/farkon00/pyauto-compl",
        packages=setuptools.find_packages(),
        python_requires=">=3.6",
        license="MIT",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
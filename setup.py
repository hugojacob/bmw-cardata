"""
BMW CarData Charging Report Generator

(C) Hugo Drumond Jacob <hugo.jacob@bmw.de>

SPDX-License-Identifier: MIT
"""

import pathlib
import setuptools

THIS_DIR = pathlib.Path(__file__).parent
setuptools.setup(
    name="bmw-cardata",
    version="0.0.1-alpha.1",
    description="BMW CarData Charging Report Generator",
    author="Hugo Drumond Jacob",
    author_email="hugodj@gmail.com",
    url="https://github.com/hugojacob",
    license="MIT",
    download_url="https://github.com/hugojacob/bmw-cardata",
    install_requires=(THIS_DIR / "requirements.txt").read_text().splitlines(),
    python_requires=">=3.8",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["bmw_cardata=bmw_cardata.cli:main"],
    },
)

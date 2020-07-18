#!/usr/bin/env python3

""" Setup file for pytemplate package.
"""
import sys

from setuptools import setup, find_packages
from pkg_resources import VersionConflict, require

import pytemplate

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(
        name=pytemplate.__title__,
        version=pytemplate.__version__,
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        packages=find_packages(exclude=["tests"]),
        install_requires=[],
        include_package_data=True,
        zip_safe=False,
        # Uncomment if needed
        # entry_points={"console_scripts": ["pytemplate=pytemplate.__main__:main"]},
        author=pytemplate.__author__,
        author_email=pytemplate.__author_email__,
        description=pytemplate.__description__,
        license=pytemplate.__license__,
        keywords=pytemplate.__keywords__,
        url=pytemplate.__url__,
        project_urls=pytemplate.__project_urls__,
    )

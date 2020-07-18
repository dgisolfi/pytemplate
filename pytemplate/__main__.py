#!/usr/bin/env python3

"""Main Entry point for the package

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>

Usage
-----
    python3 -m template
"""

from pytemplate import __project_urls__
from pytemplate.utils.logger import Logger


def main():
    # initialize logger
    logger = Logger(logging_level="DEBUG", file_log_level="OFF").logger
    logger.debug("tap tap...is this thing on?")
    logger.warning("Yes it's on...Now dont say anything stupid everyone can hear you!")
    logger.critical(
        "HELLO! WE GOT BIG ISSUES!...THIS PROJECT NEEDS TO ACTUALLY DO SOMETHING"
    )
    logger.info("Nevermind those guys, onto the main event...")
    logger.info("Hello! This is a template python package.")
    logger.info(f"Feel free to suggest additions at {__project_urls__['Bugs']}new?assignees=&labels=enhancement&template=feature_request.md&title=")


if __name__ == "__main__":
    main()

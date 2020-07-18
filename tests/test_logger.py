#!/usr/bin/env python3

"""
Author(s)
------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>
"""

import os
import json

import pytest

from pytemplate.utils.logger import Logger

# TODO: This is what you call good tests? pfffff...weak


class TestLogger:
    def testSingleInstance(self):
        # instantiate logger with level of info
        logger = Logger("INFO", "off", False)
        assert logger.logging_level == "INFO"
        # attempt to re-instantiate logger with different log level
        logger = Logger("off", "off", False)
        # ensure a new logger was not created.
        assert logger.logging_level == "INFO"

    def testLogging(self):
        # can we get the instance of the logger from the singleton?
        logger = Logger().logger
        assert logger != None
        logger.info("We can log!")

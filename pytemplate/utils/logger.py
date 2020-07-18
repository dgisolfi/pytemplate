#!/usr/bin/env python3

"""A Singleton Logger

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>
"""
import sys
import logging
from datetime import datetime


class Logger:
    """Singleton Logger Class - He was number 1!
    
    A wrapper around the actual logger class to restrict multiple instances
    """

    class __Logger:
        """The real Logger class

        Handles all logging
        """

        def __init__(
            self, logging_level: str, file_log_level: str, verbose: str,
        ):
            """actual logger constructor 
            
            Parameters
            ----------
            logging_level : str
                a valid log level for the logger
            file_log_level : str
                log level for file logging
            verbose : str
                forces debug log level
            """
            self.__logging_level = logging_level
            self.__file_log_level = file_log_level
            self.__verbose = verbose
            self.__log_file_name = ""
            self.__logger = logging.getLogger()

            formatter = logging.Formatter(
                "%(asctime)s.%(msecs)03d - %(levelname).4s - %(message)s", "%H:%M:%S",
            )

            if self.verbose is True:
                # overwrite the log levels
                self.__logging_level = "DEBUG"
                self.__file_log_level = "DEBUG"

            # set default log level
            self.__logger.setLevel(logging.getLevelName(self.__logging_level))

            if self.logging_level != "OFF":
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.getLevelName(self.__logging_level))
                console_handler.setFormatter(formatter)

                self.__logger.addHandler(console_handler)

            if self.__file_log_level != "OFF":
                self.__log_file_name = f"{datetime.now().strftime('%m%d%y%H%M%S')}.log"

                file_handler = logging.FileHandler(self.__log_file_name)
                file_handler.setLevel(logging.getLevelName(self.__file_log_level))
                file_handler.setFormatter(formatter)

                self.__logger.addHandler(file_handler)

            self.__logger.debug("Logger initialized")

        @property
        def logging_level(self):
            return self.__logging_level

        @property
        def file_log_level(self):
            return self.__file_log_level

        @property
        def verbose(self):
            return self.__verbose

        @property
        def log_file_name(self):
            return self.__log_file_name

        @property
        def logger(self):
            return self.__logger

        def error(self, return_code: int, msg: str):
            self.logger.error(msg)
            sys.exit(return_code)

    # The single instance of __Logger
    instance = None

    def __init__(
        self,
        logging_level: str = "INFO",
        file_log_level: str = "OFF",
        verbose: str = False,
    ):
        # Creates the initial instance if the logger
        if not Logger.instance:
            Logger.instance = Logger.__Logger(
                logging_level.upper(), file_log_level.upper(), verbose
            )

    # Provides access to the singleton logger class attributes
    def __getattr__(self, name):
        return getattr(self.instance, name)

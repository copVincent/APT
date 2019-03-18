#!/usr/bin/env python

import logging
import sys
from lib.core.custom import CUSTOM_LOG

logging.addLevelName(CUSTOM_LOG.SYSINFO, "*")
logging.addLevelName(CUSTOM_LOG.SUCCESS, "+")
logging.addLevelName(CUSTOM_LOG.ERROR, "-")
logging.addLevelName(CUSTOM_LOG.WARNING, "!")

LOGGER = logging.getLogger("TookitLogger")

LOGGER_HANDLER = None

try:
    from thirdparty.ansistrm.ansistrm import ColorizingStreamHandler

    try:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
    except Exception:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

except ImportError:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CUSTOM_LOG.WARNING)

class MY_LOGGER:
    @staticmethod
    def success(msg):
        return LOGGER.log(CUSTOM_LOG.SUCCESS, msg)

    @staticmethod
    def info(msg):
        return LOGGER.log(CUSTOM_LOG.SYSINFO, msg)

    @staticmethod
    def warning(msg):
        return LOGGER.log(CUSTOM_LOG.WARNING, msg)

    @staticmethod
    def error(msg):
        return LOGGER.log(CUSTOM_LOG.ERROR, msg)

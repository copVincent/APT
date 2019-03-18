#!/usr/bin/env python

import os
import subprocess

VERSION = '0.1.0'
PROJECT = "APT-Auto PenTest"
AUTHOR = 'copVcent'
MAIL = 'madichong@163.com'
PLATFORM = os.name
IS_WIN = subprocess.mswindows

# essential methods/functions in custom scripts/PoC (such as function poc())
ESSENTIAL_MODULE_METHODS = ['poc']
# Encoding used for Unicode data
UNICODE_ENCODING = "utf-8"
# String representation for NULL value
NULL = "NULL"
# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"

ISSUES_PAGE = "https://github.com/Xyntax/POC-T/issues"
GIT_REPOSITORY = "git://github.com/Xyntax/POC-T.git"
GIT_PAGE = "https://github.com/Xyntax/POC-T"

BANNER = """\033[01;34m
                                             \033[01;31m__/\033[01;34m
    ____            ____      ______\033[01;33m/ \033[01;31m__/\033[01;34m
   / __ \          / __ \    /__  __/\033[01;33m_/\033[01;34m
  / /__\ \        / /_/ /      / /
 / /____\ \      / /___/      / /
/ /      \ \    /_/          /_/
    \033[01;37m{\033[01;m Version %s by %s mail:%s \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR, MAIL)

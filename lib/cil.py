import os.path
import traceback

from lib.core.common import set_path
from lib.core.exception import *


def main():
    #在命令行运行时的主要功能
    try:
        #设定根目录
        path_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        try:
            os.path.isdir(path_ROOT)
        except:
            error = '软件目录错误，或检查系统编码'


        set_path(path_ROOT)

    except:
        print('errrrrrr')
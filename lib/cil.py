import os.path
import traceback
from lib.core.data import logger
from lib.parse.help import cmdLineParser
from lib.core.data import
from lib.core.common import set_path



def main():
    #在命令行运行时的主要功能
    try:
        #设定根目录
        path_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        try:
            #Python3默认编码为utf-8，应该不存在无法识别的编码
            #为了以防万一还是加上这句
            os.path.isdir(path_ROOT)
        except:
            error = '目录或编码错误，请检查目录中是否含有非ASK-II字符'
            logger.error(error)
            raise SystemExit

        set_path(path_ROOT)  #设置文件路径







    except:
        print('errrrrrr')
import os
from lib.core.exception import *

def set_path(path_ROOT):
    """
    设置项目目录和文件绝对路径
    """
    root_path = path_ROOT
    path_DATA = os.path.join(root_path,'data')
    path_SCRIPT = os.path.join(root_path,'script')
    path_OUTPUT = os.path.join(root_path,'output')
    path_CONFIG = os.path.join(root_path,'toolkit.conf')
    if not os.path.exists(path_DATA):
        os.mkdir(path_DATA)
    if not os.path.exists(path_SCRIPT):
        os.mkdir(path_SCRIPT)
    if not os.path.exists(path_OUTPUT):
        os.mkdir(path_OUTPUT)


    path_LESS_PASS = os.path.join(path_DATA,'pass100.txt')
    path_LARGE_PASS = os.path.join(path_DATA,'pass1000.txt')
    path_USER_AGENTS = os.path.join(path_DATA, "user-agents.txt")
    if os.path.isfile(path_USER_AGENTS) and os.path.isfile(path_LARGE_PASS) and os.path.isfile(path_LESS_PASS) and os.path.isfile(path_CONFIG):
        pass
    else:
        message = '部分文件缺失，请检查本软件的完整性\n'
        print(message)
        raise ToolkitMissingPrivileges(message)
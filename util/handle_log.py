import logging
from util.handle_yaml import Handle_yaml
import time



class Handle_Log(logging.Logger):
    #继承Logger类
    def __init__(self,name='root',level='Debug',file=None,format=None):
        super().__init__(name)
        self.setLevel(level)
        fmt=logging.Formatter(format)
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
            # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)

# 从yaml配置文件中读取logging相关配置
str =Handle_yaml("config/logConfig.yaml").read_yaml()
logger_name=str.get("logger").get("name")
log_level=str.get("logger").get("level")
log_format=str.get("logger").get("format")
#每天的日志放置在同一个文件中，错误和非错误的日志单独存放
error_file = "log/" + time.strftime("%Y-%m-%d", time.localtime()) + ".error.txt"
normal_file = "log/" + time.strftime("%Y-%m-%d", time.localtime()) + ".normal.txt"

#配置
error_logger = Handle_Log(name=logger_name,level=log_level,
                           file=error_file,
                           format=log_format)
normal_logger = Handle_Log(name=logger_name,level=log_level,
                           file=normal_file,
                           format=log_format)



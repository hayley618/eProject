import logging
import os

class Logger:
    def __init__(self):
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler,用于写入文件
        log_path = os.path.dirname(os.getcwd())+'/logs/'   # 指定文件输出路径
        log_name = log_path + 'out.log'    # 指定输出的文件名
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler,用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

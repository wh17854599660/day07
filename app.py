"""
框架搭建：
    核心：api + case + data
        api:封装请求业务（requests）
        case:集成unittest实现，调用api以及参数化解析data
        data：封装测试数据

    报告：report + tools + run_suite.py
        report:保存测试报告
        tools:封装工具文件
        run_suite.py:组织测试套件

    配置：app.py
        app.py：封装程序常量以及配置信息

    日志：log
        log:保存日志文件

"""
import logging
import os
import logging.handlers
# 封装接口的URL前缀
import token

BASE_URL = "http://182.92.81.159"

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)

# print("动态获取项目绝对路径：",PRO_PATH)

# 定义一个变量
TOKEN = None

USER_ID = None


# 生成日志
def my_log_config():
    # 获取日志对象
    logger = logging.getLogger()
    # 配置输出级别
    logger.setLevel(logging.INFO)
    # 配置输出目标--系统默认目标
    to_1 = logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + '/log/my_log.log', when='h', interval=2,
                                                     backupCount=1, encoding='utf-8')
    # 配置输出格式
    formatter = logging.Formatter \
        ("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 组合格式与输出目标和日志对象组合
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)


# 调用：在需要的位置调用日志
# 需求：为测试类的测试函数添加日志输出
#实现：
# 步骤1：包下的__init__.py初始化日志配置
#         import app
#         app.my_log_config
# my_log_config()
# logging.warning('警告')

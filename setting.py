# coding:utf-8
# @Author: zlq
"""
数据库等一系列的配置
"""


class Setting(object):
    # 主库
    # 用户名：root, 密码：123456
    MYSQL_MASTER_URL = "mysql://root:123456@127.0.0.1:3306/test_master_slave?charset=utf8"

    # 从库
    # 用户名：zhang, 密码：123456
    MYSQL_SLAVE_URL = "mysql://zhang:123456@192.168.10.168:3306/test_master_slave?charset=utf8"


    


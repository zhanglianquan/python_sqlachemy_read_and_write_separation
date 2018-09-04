# coding:utf-8
# @Author: zlq
"""
方案1：使用装饰器
"""
from sqlalchemy import create_engine
from setting import Setting
from sqlalchemy.orm import scoped_session, sessionmaker
import pymysql

# 初始化mysql连接
pymysql.install_as_MySQLdb()

master_engine = create_engine(Setting.MYSQL_MASTER_URL, echo=False)
slave_engine = create_engine(Setting.MYSQL_SLAVE_URL, echo=False)
Session = scoped_session(sessionmaker(bind=master_engine))


# 保证永远使用从库, 不用这个装饰的， 使用的是主库
def with_slave(fn):
    def go(*arg, **kw):
        s = Session()
        oldbind = s.bind
        s.bind = slave_engine
        try:
            return fn(*arg, **kw)
        finally:
            s.bind = oldbind
    return go



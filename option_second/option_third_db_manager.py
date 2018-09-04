# coding:utf-8
# @Author: zlq

"""
方案2：使用自定义的数据库管理器
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from setting import Setting
import contextlib
import pymysql
import random
# 初始化mysql连接
pymysql.install_as_MySQLdb()


class DBManager(object):

    def __init__(self):
        self.session_map = {}
        self.create_sessions()

    def create_sessions(self):
        db_settings = {'master': Setting.MYSQL_MASTER_URL,
                       'slave': Setting.MYSQL_SLAVE_URL
                       }
        for role, url in db_settings.items():
            self.session_map[role] = self.create_single_session(url)

    @classmethod
    def create_single_session(cls, url, scopefunc=None):
        engine = create_engine(url, echo=False)
        return scoped_session(
            sessionmaker(
                expire_on_commit=False,
                bind=engine
            ),
            scopefunc=scopefunc
        )

    def get_session(self, name):
        try:
            if not name:
                # 当没有提供名字时，我们默认为读请求，
                # 现在的逻辑是在当前所有的配置中随机选取一个数据库，
                # 你可以根据自己的需求来调整这里的选择逻辑
                name = random.choice(self.session_map.keys())

            return self.session_map[name]
        except KeyError:
            raise KeyError('{} not created, check your DB_SETTINGS'.format(name
                                                                           ))
        except IndexError:
            raise IndexError('cannot get names from DB_SETTINGS')

    @contextlib.contextmanager
    def session_ctx(self, bind=None):
        DBSession = self.get_session(bind)
        session = DBSession()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.expunge_all()
            session.close()



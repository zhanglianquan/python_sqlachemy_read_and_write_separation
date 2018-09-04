# coding:utf-8
# @Author: zlq

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from setting import Setting
import pymysql

# 初始化mysql连接
pymysql.install_as_MySQLdb()

BaseModel = declarative_base()


class User(BaseModel):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))


def get_master_db_session():
    master_engine = create_engine(Setting.MYSQL_MASTER_URL, echo=False)
    BaseModel.metadata.create_all(master_engine)
    return scoped_session(sessionmaker(bind=master_engine))


def get_slave_db_session():
    # 注意使用前， 配置mysql的主从同步机制， 不会的google
    slave_engine = create_engine(Setting.MYSQL_SLAVE_URL, echo=False)
    return scoped_session(sessionmaker(bind=slave_engine))



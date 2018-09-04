# coding:utf-8
# @Author: zlq
"""
python(flask , tornado) + mysql (sqlalchemy)的读写分离
使用架构是： 主从同步(一主一从) + 读写分离
"""
from model import User, get_master_db_session, get_slave_db_session
import random
"""
"""


# 每次写入主库100条测试数据
def write_data_to_master_db(session):

    objects = []

    def __write_data(item):
        user_model = User()
        password = str(random.randint(123456, 654321))
        user_model.password = password
        user_model.username = "zhangsan" + password
        objects.append(user_model)
    [__write_data(item) for item in range(0, 100)]
    session.flush()
    session.add_all(objects)
    session.commit()


if __name__ == "__main__":

    """
     重要的事情说三遍
     # 注意使用前， 配置mysql的主从同步机制， 不会的google
     # 注意使用前， 配置mysql的主从同步机制， 不会的google
     # 注意使用前， 配置mysql的主从同步机制， 不会的google
    """
    master_session = get_master_db_session()
    """
    # 测试主从同步：主库每次写好100条数据， 从库同步数据，
    #  如果从库有了，数据，说明主从同步配置ok了
    """
    # 测试主从同步
    write_data_to_master_db(master_session)

    # 下面都是要去各自的模块运行， 才能测试读写分离
    """
        重要的事情说三遍
        # 读写分离 测试 ， 分别可用option_first, option_second, option_third
        # 三种方案模块, 的read_slave和write_master 模块测试
        
        # 读写分离 测试 ， 分别可用option_first, option_second, option_third
        # 三种方案模块, 的read_slave和write_master 模块测试
        
        # 读写分离 测试 ， 分别可用option_first, option_second, option_third
        # 三种方案模块, 的read_slave和write_master 模块测试
    """





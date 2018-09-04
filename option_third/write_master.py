# coding:utf-8
# @Author: zlq

"""
主库写
"""
from option_third.option_third_func import get_master_db_session
from model import User
import random
import time

Session = get_master_db_session()


def my_write_view():
    # 每次写入主库10条测试数据
    print("*" * 30)
    print("option_first ------my_write_view")
    objects = []

    def __write_data(item):
        user_model = User()
        password = str(random.randint(123456, 654321))
        user_model.password = password
        user_model.username = "zhangsan" + password
        objects.append(user_model)

    [__write_data(item) for item in range(0, 10)]
    Session.flush()
    Session.add_all(objects)
    Session.commit()


if __name__ == "__main__":
    # 这个线程从主库写
    while 1:
        my_write_view()
        time.sleep(4)


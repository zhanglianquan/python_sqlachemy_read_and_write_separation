# coding:utf-8
# @Author: zlq
"""
从库读
"""
from option_first.option_first_deco import Session, with_slave
from model import User
import random
import time


@with_slave
def my_read_view():
    print("*"*30)
    print("option_first ------my_read_view")
    # user_id = random.randint(1600, 1800)
    user_id = 1942
    query_result = Session.query(User).filter(User.id == user_id).first()
    if query_result:
        print(" exist's data  user id={id}".format(id=user_id))
        print(query_result.username)
    else:
        print(" no exist's data  user id={id}".format(id=user_id))


if __name__ == "__main__":
    # 这个线程从从库读
    while 1:
        my_read_view()
        time.sleep(2)


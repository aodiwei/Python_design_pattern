#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/14'
# 
"""


class SingletonClassic:
    """
    经典方式：相当于增加一个类变量来记录这个类是否被创建了，如果有这个类变量说明被创建了
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


def te_singleton_classic():
    """
    测试SingletonClassic
    :return:
    """
    s0 = SingletonClassic()
    print(s0)
    s1 = SingletonClassic()
    print(s1)

    print('s0 == s1: {}'.format(s0 == s1))


class SingletonLazy:
    """
    懒汉模式:在需要时才创建
    """
    __instance = None

    def __init__(self):
        if SingletonLazy.__instance:
            raise SyntaxError('SingletonLazy need SingletonLazy.get_instance() function to instance')
        SingletonLazy.__instance = self
        # raise NotImplementedError
        # if not SingletonLazy.__instance:
        #     print('do nothing')
        # else:
        #     print('created....')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()

        return cls.__instance


def te_singleton_lazy():
    """

    :return:
    """
    s0 = SingletonLazy()  # 只能用一次，最好每次直接用SingletonLazy.get_instance()
    print(s0)
    s1 = SingletonLazy.get_instance()
    print(s1)
    s3 = SingletonLazy.get_instance()
    print(s3)
    # s2 = SingletonLazy()
    # print(s2)


def singleton(cls):
    """
    装饰器的方式
    :param cls:
    :return:
    """
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class AnyClass:
    pass


def te_singleton_dec():
    s0 = AnyClass()
    print(s0)
    s1 = AnyClass()
    print(s1)


if __name__ == '__main__':
    te_singleton_classic()
    # te_singleton_lazy()
    # te_singleton_dec()

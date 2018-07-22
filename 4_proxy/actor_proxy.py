#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/21'
# 代理模式
"""


class Actor:
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, 'is occupied with current movie')

    def avaliable(self):
        self.is_busy = False
        print(type(self).__name__, 'is free for the movie')

    def get_status(self):
        return self.is_busy


class Agent:
    def __init__(self):
        self.principal = None

    def work(self):
        # 可以操作很多actor,对外只有work
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.avaliable()


if __name__ == '__main__':
    r = Agent()
    r.work()

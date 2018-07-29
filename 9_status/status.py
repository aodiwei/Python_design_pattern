#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/28'
# 
"""


class ComputerState:
    name = 'status'
    allowed = []  # 当前状态在allowed里的情况才能转为name

    def switch(self, state):
        if state.name in self.allowed:
            print('Current: {} => switched to new status: {}'.format(self, state.name))
            self.__class__ = state
        else:
            print('Current: {} => switching to {} not possible'.format(self, state.name))

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


# 挂起
class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


# 休眠
class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer:
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()
    comp.change(On)

    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)

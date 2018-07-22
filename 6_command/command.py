#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/22'
# 
"""
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        super().__init__(recv)

    def execute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print('Receiver Action')


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)  # 绑定
    invker = Invoker()
    invker.command(cmd)  # 只关注cmd对象，不关注具体业务的recv
    invker.execute()

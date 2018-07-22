#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/22'
# 
"""
from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def template(self):
        """
        模板流程，子类实现抽象方法，然后调用此方法，执行模板流程
        :return:
        """
        self.collect_source()
        self.compile_to_object()
        self.run()


class IOSCompliler(Compiler):
    def collect_source(self):
        print('collecting swift source code')

    def compile_to_object(self):
        print('compiling swift code to LLVM bitcode')

    def run(self):
        print('Program running on runtime environment')


if __name__ == '__main__':
    IOS = IOSCompliler()
    IOS.template()

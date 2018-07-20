#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/14'
# 简单工厂模式，根据类型创建实例
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('wang wang')


class Cat(Animal):
    def do_say(self):
        print('miao miao')


# 森林工厂

class ForestFactory:
    def make_sound(self, ob_type):
        return eval(ob_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    an = 'Dog'
    ff.make_sound(an)
    an = 'Cat'
    ff.make_sound(an)

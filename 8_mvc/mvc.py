#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/28'
# 
"""


class Model:

    def logic(self):
        """
        一些数据结构，比如数据库表之类
        :return:
        """
        data = 'Got it'
        print('Model: get some data')
        return data


class View:
    def update(self, data):
        print('View: updating view with model data=>{}'.format(data))


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print('Controller: Relayed the Client asks')
        data = self.model.logic()
        self.view.update(data)


if __name__ == '__main__':
    controller = Controller()
    controller.interface()

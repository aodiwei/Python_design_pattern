#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/22'
#
"""

from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """
    Command基类
    """

    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    """
    相当于ConcreteCommand
    """

    def __init__(self, recv):
        super().__init__(recv)

    def execute(self):
        self.recv.buy()


class SellStockOrder(Order):
    """
    相当于ConcreteCommand
    """

    def __init__(self, recv):
        super().__init__(recv)

    def execute(self):
        self.recv.sell()


class StockTrade:
    """
    相当于receiver,具体业务
    """

    def action(self):
        print('Receiver Action')

    def buy(self):
        print('buy.......')

    def sell(self):
        print('sell..........')


class Agent:
    """
    Invoker
    """
    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    stock = StockTrade()
    buy = BuyStockOrder(stock)
    sell = SellStockOrder(stock)

    agent = Agent()
    agent.place_order(buy)
    agent.place_order(sell)
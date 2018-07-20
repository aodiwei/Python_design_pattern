#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/20'
# 抽象工厂方法： 类爆炸
"""
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare DeluxVeggiePizza', type(self).__name__)


class ChickenPizza(NonVegPizza):

    def serve(self, VegPizza):
        print(type(self).__name__, ' is served with Ham on ', type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare MexicanVegPizza', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, ' is served with Ham on ', type(VegPizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.create_non_veg_pizza()
            self.VegPizza = self.factory.create_veg_pizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)
            print('*************')


pizza = PizzaStore()
pizza.make_pizzas()

#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/22'
# 
"""
from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return 'Got News:', self.__latest_news


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for sub in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        sub(news_publisher)

    print('subscribers: {}'.format(news_publisher.subscribers()))
    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()

    print('detached: {}'.format(type(news_publisher.detach()).__name__))
    print('subscribers: {}'.format(news_publisher.subscribers()))

    news_publisher.add_news('Big news')
    news_publisher.notify_subscribers()
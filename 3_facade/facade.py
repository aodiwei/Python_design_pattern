#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/21'
# 门面模式
"""


class EventManager:

    def __init__(self):
        print('Event Manager:: Let me talk to the folks\n')

    def arrange(self):
        """
        门面内容，对外接口
        :return:
        """
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier:
    def __init__(self):
        print('Arranging the Hotle for Marriage? --')

    def __is_available(self):
        print('Is the Hotel free for the event on given day?')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Registered the Booking\n\n')


class Florist:
    def __init__(self):
        print('Flower Decorations for the Event? --')

    def set_flower_requirements(self):
        print('Carnations, Roses and Lilies would e used for Decorations\n\n')


class Caterer:
    def __init__(self):
        print('Food Arrangements for the Event --')

    def set_cuisine(self):
        print('Chinese & Continental Cuisine to be served\n\n')


class Musician:
    def __init__(self):
        print('Musical Arrangements for the Marriage --')

    def set_music_type(self):
        print('Jazz and Classical will be played\n\n')


class You:
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements?? !!!')

    def ask_event_manager(self):
        print('You:: Let us Contact the Event Manager\n\n')

        em = EventManager()
        em.arrange()


if __name__ == '__main__':
    y = You()
    y.ask_event_manager()

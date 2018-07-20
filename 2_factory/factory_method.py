#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'David Ao'
__mtime__ = '2018/7/14'
# 工厂方法模式，由子类来决定创建哪些类
"""
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('个人信息 section')


class AlbumSection(Section):
    def describe(self):
        print('头像 section')


class PatentSection(Section):
    def describe(self):
        print('专利 section')


class PublicationSection(Section):
    def describe(self):
        print('出版物 section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()
        self.describe()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)

    def describe(self):
        for s in self.sections:
            s.describe()


class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    p_type = 'Linkedin'
    pro = eval(p_type)()
    ret = pro.get_sections()
    print(ret)
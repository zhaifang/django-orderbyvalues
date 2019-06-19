# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(

      name="django-orderbyvalues",

      version="0.1",

      description="make QuerySet can order by values",

      author="ZhaiFang",

      url="https://github.com/zhaifang/django-orderbyvalues",

      license="MIT",

      packages= find_packages(),

      scripts=["django_orderbyvalues/django_orderbyvalues.py"],

      )
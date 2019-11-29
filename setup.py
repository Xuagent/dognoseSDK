# -*- coding:utf-8 -*-
# Author: Agent Xu

from setuptools import setup, find_packages

with open('README.md','r',encoding='utf-8') as f:
	data = f.read()

setup(
	name = "demo",
	version = "0.1",
	url = 'https://github.com/Xuagent/Yolov3-tiny-dognose.git',
	long_description = data,
	packages = find_packages(),
)

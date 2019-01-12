#coding=utf8

from setuptools import setup

long_description = """
https://github.com/taojy123/SettingsCloud

云端储存项目配置的敏感参数，拒绝使用 local_settings 造成代码管理的混乱

Python 客户端
"""

setup(
    name='pysettingscloud',
    version='0.1.4',
    description='SettingsCloud 的 python 客户端',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='tao.py',
    author_email='taojy123@163.com',
    maintainer='tao.py',
    maintainer_email='taojy123@163.com',
    install_requires=['requests'],
    license='MIT License',
    py_modules=['pysettingscloud'],
    platforms=["all"],
    url='https://github.com/taojy123/SettingsCloud/tree/master/clients/python',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)

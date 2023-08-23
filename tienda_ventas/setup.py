from setuptools import setup

setup (
    name='pv',
    version='0.1',
    py_modules=['tv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tv=tv:cli
    ''',
)
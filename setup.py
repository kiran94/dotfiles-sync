from setuptools import setup

setup(
    name='dotfiles',
    version='0.0.1',
    packages = ['dotfiles'],
    entry_points = {
        'console_scripts': [
            'dotfiles = dotfiles.__main__:main'
        ]
    }
)
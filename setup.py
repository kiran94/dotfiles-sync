from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read()
    requirements = requirements.split('\n')

setup(
    name='dotfiles-sync',
    version='0.0.1',
    packages=['dotfiles'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'dotfiles = dotfiles.__main__:main'
        ]
    }
)

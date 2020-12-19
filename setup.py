from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read()
    requirements = requirements.split('\n')

setup(
    name='dotfiles-sync',
    version='0.0.2',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'dotfiles = dotfiles.__main__:main'
        ]
    }
)

from setuptools import setup, find_packages

with open("README.md", "r") as desc:
    long_description = desc.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()
    requirements = requirements.split('\n')

setup(
    name='dotfiles-sync',
    version='0.0.5',
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Manages dotfile configuration files across operating systems",
    url="https://github.com/kiran94/dotfiles-sync",
    entry_points={
        'console_scripts': [
            'dotfiles = dotfiles.__main__:main'
        ]
    },
    keywords='dotfiles',
    python_requires='>=3.6',
    license='MIT'
)

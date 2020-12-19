# dotfiles-sync

![Deploy](https://github.com/kiran94/dotfiles-sync/workflows/Deploy/badge.svg) ![pypi](https://img.shields.io/pypi/v/dotfiles-sync)

dotfiles-sync is a command line application which helps manage configuration files (typically dotfiles) across different machines and operating systems. 

- [dotfiles-sync](#dotfiles-sync)
  - [Motivation](#motivation)
  - [Getting Started](#getting-started)
    - [`list`](#list)
    - [`sync`](#sync)
    - [`update`](#update)

## Motivation

I needed a solution which would allowed me to easily automate synchronising my configuration files as I jump between different machines which could be either Windows or Linux.

## Getting Started

This package is deployed to [pypi](https://pypi.org/project/dotfiles-sync/):

```sh
python -m pip install dotfiles-sync
```


The `--help` will always show the most up to date options:

```sh
❯ dotfiles --help
usage: dotfiles [-h] [-c CONFIG] [-w CONFIG_DIR] [-d] [-i] {list,sync,update} ...

positional arguments:
  {list,sync,update}

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        dotfiles configuration. Points to target locations.
  -w CONFIG_DIR, --config_dir CONFIG_DIR
                        Location of the configuration files to sync
  -d, --dry             Never actually write any files, only read and show me what you would have done
  -i, --interactive     Before doing a write, ask for confirmation
```

This application relies on the fact that you store your configuration in source control and that you define a configuration file which declares your configurations you want to track along with paths per operating system. 

An example of a configuration file is:

```sh
{
    "config": 
    {
        ".bashrc": 
        {
            "Linux": "~/.bashrc",
            "Windows": "~/.bashrc"
        }
    }
}
```

Where `.bashrc` is the file in the *configuration directory* we are interested in tracking. The *configuration directory* is the directory where the central authrority of that file lives (typically a git repository which contains all your configuration files). This key could also be directory e.g `bash/.bashrc` if you wanted to keep all your bash related configuration files in organised into a `bash` folder.

Each key contains paths to operating system specific path the file should be syncronised into. The operating systems supported here are the same as the ones that come in [platform.system](https://docs.python.org/3/library/platform.html#platform.system). Paths are also expanded using [os.path.expanduser](https://docs.python.org/3/library/os.path.html#os.path.expanduser) which means special symbols like `~` will be expanded in both Window and Linux.

### `list`

Once you have a dotfiles configuration and configuration directory you can run `list`:

```sh
❯ dotfiles --config examples/config.json --config_dir examples/configs list
[18:58:55] INFO     Listing Configurations
           INFO     .bashrc: examples/configs/.bashrc => /home/kiran/.bashrc (ConfigurationMatchStatus.SYNCHRONIZABLE | ConfigurationFileType.FILE)
           INFO     .vimrc: examples/configs/.vimrc => /home/kiran/.vimrc (ConfigurationMatchStatus.SYNCHRONIZABLE | ConfigurationFileType.FILE)
           INFO     pgcli: examples/configs/pgcli => /home/kiran/.config/pgcli (ConfigurationMatchStatus.SYNCHRONIZABLE | ConfigurationFileType.DIRECTORY)
```

`SYNCHRONIZABLE` means it looks like it is possible to synchronise this file and `FILE` tells us the type of synchronize it's going to do (as oppsosed to `DIRECTORY` which will do a recursive copy).

### `sync`

If we are happy, then we can do a `sync`. This will take the files in your configuration directory and allow them to the machine.

```sh
❯ dotfiles --config examples/config.json --config_dir examples/configs sync

[18:59:41] INFO     Copying File examples/configs/.bashrc => /home/kiran/.bashrc
           INFO     Copying File examples/configs/.vimrc => /home/kiran/.vimrc
           INFO     Copying Directory examples/configs/pgcli => /home/kiran/.config/pgcli
Syncing Configuration... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```

### `update`

You may want to also do the reverse and update your configuration directory with the files on your current machine. This can be done using `update`:

```sh
❯ dotfiles --config examples/config.json --config_dir examples/configs update

[19:01:47] INFO     Copying File /home/kiran/.bashrc => examples/configs/.bashrc
           INFO     Copying File /home/kiran/.vimrc => examples/configs/.vimrc
           INFO     Copying Directory /home/kiran/.config/pgcli => examples/configs/pgcli
Updating Configuration Directory: examples/configs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```
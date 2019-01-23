# splitdir

## Description

split large directory to given number of sub directory

## Installation

```bash
$ git clone https://github.com/rwseg/splitdir.git
$ cd splitdir
$ python setup.py install
```

## Usage

```
usage: splitdir [-h] -d DIRECTORY [-c COUNT] [-p PREFIX] [-o OUTDIR]

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        the directory you want to split
  -c COUNT, --count COUNT
                        how many sub directories, default how many core your
                        cpu has
  -p PREFIX, --prefix PREFIX
                        sub directory prefix
  -o OUTDIR, --outdir OUTDIR
                        where to save your sub directories
```
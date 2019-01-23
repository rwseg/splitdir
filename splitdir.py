# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import argparse
import multiprocessing
from shutil import copyfile, copytree

"""
Author: rwsieng@gmail.com
split large directory to multiple sub directories according to given size
"""


__version__ = '1.0'
__all__ = [
    'split',
]


def check_positive(value):
    """check if the count number is greater than 1"""
    ivalue = int(value)
    if ivalue <= 1:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def check_directory(directory):
    """check if the directory existed"""
    if os.path.exists(directory):
        return os.path.abspath(directory)
    raise argparse.ArgumentTypeError('invalid directory: %s' % directory)


def split():
    """main split function"""
    parser = argparse.ArgumentParser('splitdir', description=__doc__)
    parser.add_argument('-d', '--directory', help='the directory you want to split', required=True, type=check_directory)
    parser.add_argument('-c', '--count', help='how many sub directories, default how many core your cpu has', required=False, type=check_positive)
    parser.add_argument('-p', '--prefix', help='sub directory prefix', required=False)
    parser.add_argument('-o', '--outdir', help='where to save your sub directories', required=False, type=check_directory)
    args = parser.parse_args()

    if not args.count:
        args.count = multiprocessing.cpu_count()
    if not args.prefix:
        args.prefix = os.path.basename(os.path.normpath(args.directory))
    if not args.outdir:
        args.outdir = os.path.dirname(os.path.normpath(args.directory))
    fs = os.listdir(args.directory)
    total = len(fs)
    if total >= args.count:
        # split balancely
        chunk_size = total // args.count
        surplus = total % args.count
        part_1 = fs[:total-surplus]
        part_2 = fs[total-surplus:]
        sub_fs_list = [part_1[i: i+chunk_size] for i in range(0, len(part_1), chunk_size)]
        for sub_fs, f in zip(sub_fs_list, part_2):
            sub_fs.append(f)

        # copy to sub directory
        for i, sub_fs in enumerate(sub_fs_list):
            sub_directory = os.path.join(args.outdir, '%s_%d' % (args.prefix, i+1))
            if not os.path.exists(sub_directory):
                os.mkdir(sub_directory)
            for f in sub_fs:
                if os.path.isdir(os.path.join(args.directory, f)):
                    copytree(os.path.join(args.directory, f), os.path.join(sub_directory, f))
                else:
                    copyfile(os.path.join(args.directory, f), os.path.join(sub_directory, f))
    else:
        parser.error('Too few files.')


if __name__ == '__main__':
    split()
#!/usr/bin/env python2
import sys
import argparse
from nvlinpatch.main import main

parser = argparse.ArgumentParser()

parser.add_argument('-V', '--version', dest='version', action='store',
                    default=None,
                   help='force patcher to use patches for a specific version')
parser.add_argument('file',
                    help='the file to patch; should be either nv-kernel.o or '
                    'nvidia.ko')

args = parser.parse_args()

sys.exit(main(open(args.file,'r+b'), args.version))

#!/usr/bin/env python

import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out')
    return parser.parse_args()

def main():
    args = get_args()

if __name__ == '__main__':
    sys.exit(main())

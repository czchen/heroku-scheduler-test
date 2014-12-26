#!/usr/bin/env python
import logging


def main():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    logging.info('echo')

if __name__ == '__main__':
    main()

import sys
import os
import yaml

from latex import LatexDoc
from config import Config

CONFIG_FILE = "latexfit.yml"
        
def print_usage():
    print(f'python3 {sys.argv[0]} <FILE.tex>')
    exit(1)

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print_usage()
    try:
        file = open(sys.argv[1], 'r')
        return file
    except OSError:
        print(f'Could not open file {sys.argv[1]}')
        print_usage()

def main():
    file = parse_args()
    doc = LatexDoc(file)
    config = Config(CONFIG_FILE)
    config.apply_to(doc)
    doc.output_to(sys.stdout)

if __name__ == '__main__':
    main()
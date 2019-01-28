#!/Users/kcosta/.brew/bin/python3

import argparse
from DSLR.core import describe

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", type=str, help="input file")
  args = parser.parse_args()

  describe(args.file)

import argparse
from DSLR.core import describe

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("dataset", type=str, help="input dataset")
  args = parser.parse_args()

  describe(args.dataset)

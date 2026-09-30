import argparse

from game import DotsAndBoxes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Dots and Boxes.")
    parser.add_argument("--rows", type=int, default=2, help="Number of box rows.")
    parser.add_argument("--cols", type=int, default=2, help="Number of box columns.")
    args = parser.parse_args()
    DotsAndBoxes(args.rows, args.cols).run()

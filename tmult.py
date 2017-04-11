# File: tmult.py
# Author: Samuel McFalls

import argparse
from sys import exit

args = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
        "Given a trace file input, generate a trace file output with a " +\
        "given multiplier. Useful in CS 3214 malloc-lab.")
    parser.add_argument("infile", metavar="INPUT_FILE", help=
        "The original trace file")
    parser.add_argument("mult", metavar="MULTIPLIER", type=float,
        help="The multiplier to use")
    parser.add_argument("outfile", metavar="OUTPUT_FILE",
        help="The new trace file")

    args = parser.parse_args()

    if (args.infile == args.outfile):
        print("Cannot overwrite original file")
        exit(1)

    with open(args.infile) as infile:
        with open(args.outfile, "w") as outfile:
            for line in infile:
                tokens = line.split(" ")
                if (len(tokens) == 3):
                    # Write the multiplied version to the outfile
                    outfile.write(tokens[0] + " " + tokens[1] + " " +\
                        str(int(int(tokens[2]) * args.mult)) + "\n")
                else:
                    outfile.write(line)

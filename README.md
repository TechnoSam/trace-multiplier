# trace-multiplier
usage: tmult.py [-h] INPUT_FILE MULTIPLIER OUTPUT_FILE

Given a trace file input, generate a trace file output with a given
multiplier. Useful in CS 3214 malloc-lab.

positional arguments:

  INPUT_FILE   The original trace file

  MULTIPLIER   The multiplier to use

  OUTPUT_FILE  The new trace file

optional arguments:

  -h, --help   show this help message and exit

# Notes
Written with Python 3.6.0

Verified on Python 2.7.5 (version on CS rlogin at time of writing)

Included binary-bal.rep example file with binary3-bal.rep output from running
```
python tmult.py binary-bal.rep 0.75 binary3-bal.rep
```

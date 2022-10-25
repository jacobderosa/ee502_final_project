import os
import sys
import numpy as np
import csv

def run(args):
	parser = argparse.ArgumentParser(description="Run HW2 code")
	parser.add_argument('--download', help='Download dataset from Google Drive',
		action='store_true')
	parser.add_argument('--workdir', help='Work directory to store all outputs' default='workdir')
	args = parser.parse_args(args)	

	if args.download:
		

	return 0


if __name__=='__main__':
	exit(run(sys.argv[1:]))
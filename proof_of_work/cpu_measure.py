#!/usr/bin/python

import sys
import getopt
import time
import hashlib
from struct import unpack, pack

def usage():
	print "usage: cpu_measure -i <interval>"
	sys.exit(2)

def main(argv):
	timestamp = str(time.time())
	nonce = 0
	guess = 99999999999999999999
	payload = timestamp
	interval = 5

	try:
		opts, args = getopt.getopt(argv,"hi:",["help", "interval="])
	except getopt.GetoptError:
		print 'cpu_measure.py -i <interval>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-i", "--interval"):
			interval = float(arg)
		elif opt in ("-h", "--help"):
			usage()

	print "Beginning CPU Hash Test with Python. Interval set to %s" % interval

	payloadHash = hashlib.sha256(payload).digest()

	start = time.time()
	while start + interval > time.time():
	        nonce += 1
        	guess, = unpack('>Q',hashlib.sha256(hashlib.sha256(pack('>Q',nonce) + payloadHash).digest()).digest()[0:8])

	hashRate = nonce / interval 

	print "Total Hashes: %s" % nonce
	print "Run Time: %s" % interval
	print "Hash Rate: %s" % hashRate

if __name__ == "__main__":
   main(sys.argv[1:])

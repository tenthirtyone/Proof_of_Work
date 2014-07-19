#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:",["interval="])
   except getopt.GetoptError:
      print 'cpu_measure.py -i <interval>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--interval"):
         print 'test.py -i <inputfile> -o <outputfile>'
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])

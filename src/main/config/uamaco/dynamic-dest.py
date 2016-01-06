#!/usr/bin/python

import sys, os, re, datetime, shutil,  uuid

# read the local file from standard input
input_file=sys.stdin.readline().strip()

# make sure that we're dealing with a local file
if input_file.find("file:") != 0:
  print >> sys.stderr, "Expecting input file scheme to be 'file:': '%s'" % input_file
  sys.exit(1)

# trim away the scheme
input_file=input_file.replace("file:", "")

# make sure what we are left with is a file that exists
if not os.path.exists(input_file):
  print >> sys.stderr, "Path isn't valid: '%s'" % input_file
  sys.exit(2)

filename = os.path.basename(input_file)

if "HI360" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/csv", filename)
  print final_path
elif "hi360" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/csv", filename)
  print final_path
elif "CCLF" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/cclf", filename)
  print final_path
elif "cclf" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/cclf", filename)
  print final_path
elif "HL7" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/hl7", filename)
  print final_path
elif "hl7" in filename:
  final_path = "%s/%s" % ("hdfs://10.13.1.18:9000/data/neo/uamaco/hl7", filename)
  print final_path

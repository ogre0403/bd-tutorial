#!/usr/bin/python -u
import browndog.bd as bd
import time
import os
from os.path import isfile, join, splitext, basename

#parameters to access BD services
bds = 'https://bd-api.ncsa.illinois.edu'

# key and token from the Brown Dog API Gateway service
token = ""

# path to the folder to process
input_path = "input"

# path to the folder to store output
# add time.time() to make the output folder unique for each run
output_path = "output"+str(int(time.time()))

# output format
output_format = "pdf"

# Create a output folder
os.makedirs(output_path)

# create a list of files that is not a folder
onlyfiles = [join(input_path, f) for f in os.listdir(input_path) if isfile(join(input_path, f))]

for (input_file) in onlyfiles:
	filename, file_extension = splitext(basename(input_file))
	input_format = file_extension[1:]

	print 'File: ' + basename(input_file) + ', ' + input_format + ' to '+ output_format

	# getting possible output format by the input format
	#
	# Use bd.py to get all possible output formats for the input file type
	outputs = bd.outputs(bds, input_format, token)

	# if the output format is not supported, skip the conversion
	#
	# Search the outputs list for the desired output format
	#	if it is not a possible output format, the file will not be converted
	if not(output_format in outputs):
		print output_format, 'is not supported'
		continue
	
	# create a output file name with path
	output_file = join(output_path, filename +"." + output_format)

	# do the conversion
	#
	# Use bd.py to run the conversion
	bd.convert(bds, input_file, output_format, output_file, token, 60, True)

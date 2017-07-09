#!/usr/bin/python -u
import browndog.bd as bd
import time
import os
from os.path import isfile, join, splitext, basename

#parameters to access BD services
bds = 'https://bd-api.ncsa.illinois.edu'

# key and token from the Brown Dog API Gateway service
#
# TODO: INSERT TOKEN BETWEEN QUOTES
token = ""

# path to the folder to process
#
# TODO: INSERT INPUT PATH BETWEEN QUOTES
input_path = "input"

# path to the folder to store output
# add time.time() to make the output folder unique for each run
#
# TODO: INSERT OUTPUT PATH BETWEEN QUOTES
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
	# You could look in bd.py for the outputs function to see what arguments are needed.
	# During the tutorial you can look at the slides or the handout.
	# hint: call the function with bd.<function name>
	# TODO: ADD ONE LINE OF CODE
	
	outputs = bd.outputs(bds, input_format, token)

	# if the output format is not supported, skip the conversion
	#
	# Search the outputs list for the desired output format
	#	if it is not a possible output format, the file will not be converted
	# hint: test if the output format is not in the outputs, if not continue
	# TODO: ADD THREE LINES OF CODE
	
	if not(output_format in outputs):
		print output_format, 'is not supported'
		continue
	
	# create a output file name with path
	#
	# hint: just add the path, filename, and output format into a full path 
	# TODO: ADD ONE LINE OF CODE
	
	output_file = join(output_path, filename +"." + output_format)

	# do the conversion
	#
	# Use bd.py to run the conversion
	# You could look in bd.py for the convert function.
	# During the tutorial, you can look at the slides or the handout
	# TODO: ADD ONE LINE OF CODE	
		
	bd.convert(bds, input_file, output_format, output_file, token, 60, True)

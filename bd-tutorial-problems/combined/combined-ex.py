#!/usr/bin/python -u
import browndog.bd as bd
import time
import os
from os.path import isfile, join, splitext, basename

#parameters to access BD services
bds = 'https://bd-api.ncsa.illinois.edu'

# token from the Brown Dog API Gateway service
token = ""

# path to the folder to process
input_file = ""

# path to the folder to store output
output_path = ""+str(int(time.time()))

# output format
output_format = "png"

def main():
	# create a output folder
	os.makedirs(output_path)

	# convert the image file to png
	output = convert(input_file, output_format, output_path, bds, token)

	# extract metadata from the converted file
	metadata = extract(output, bds, token)

	# print the "tag" section for to see the face detected
	print metadata['tags']

def convert(input_file, output_format, output_path, bds, token):
	filename, file_extension = splitext(basename(input_file))
	input_format = file_extension[1:]

	print 'File: ' + basename(input_file) + ', ' + input_format + ' to '+ output_format
	
	# getting possible output format by the input format
	# Hint: use bd.outputs(__,__,__)
	outputs = 

	# create a output file name with path
	output_file = output_path + '/' + filename + "." + output_format

	# do the conversion
	return bd.convert(__, __, __, __,__, 60, True)	

def extract(extract_file, bds, token):
	print 'Processing File: ' + extract_file 
	
	#Hint: use bd.extract(__,__,__,120)
	extract_output = 
	return extract_output

if __name__ == "__main__":    
	main()

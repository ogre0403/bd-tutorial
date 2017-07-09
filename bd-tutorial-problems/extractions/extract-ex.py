#!/usr/bin/python -u
import browndog.bd as bd
import os
from os.path import isfile, join, splitext, basename

# this is the method to search dictionary by key
def findItem(obj, key):
	if key in obj: return obj[key]
	for k, v in obj.items():
		if isinstance(v, dict):
			item = findItem(v, key)
			if item is not None:
				return item

# this is the method to search key with given string
def search(values, searchFor):
	found = []
	# Here add a method that searches values for a search term.
	# Values is a dictionary of dictionaries that have lists of terms as the value.
	# 	So you will need to loop through dictionaries and search through each dictionaries values
	# 	for the searchFor value.  If it is in the list, that means you found a file 
	#	that meets your criteria and you will add that file to the found list.
	#
	# TODO: ADD FOUR LINES OF CODE HERE
	
	

	return found

#parameters to access BD services
bds = 'https://bd-api.ncsa.illinois.edu'

# key and token from the Brown Dog API Gateway service
#
# TODO: INSERT TOKEN BETWEEN QUOTES
token = ""

# path to the folder to process
#
# TODO: INSERT INPUT PATH BETWEEN QUOTES
input_path = ""

# create a list of files that is not a folder
onlyfiles = [join(input_path, f) for f in os.listdir(input_path) if isfile(join(input_path, f))]

text_store = {}

# processing the files in the given folder
for (input_file) in onlyfiles:
	filename, file_extension = splitext(basename(input_file))
	input_format = file_extension[1:]

	print 'Processing file: ' + basename(input_file) 
	
	# do the extraction
	# Use bd.py to extract metadata from the file
	# You could look in bd.py to find the function 'extract' and view the needed arguments.
	# You can call the function with bd.extract(args)
	# During the tutorial, you can look at the slides or the handout.
	#
	# TODO: ADD ONE LINE OF CODE
	

	# process the metadata 
	# find the "OCR" results and store
	#
	# Here you will need to search the metadata for an ocr result.
	# There can be many dictionaries of metadata returned.  You will need to look in metadata.jsonld,
	# by searching each object in metadata.jsonld.  As you loop through each object, you can use the findItem
	# function above to see if there is an object with key='ocr_simple' with text in it.  That is the text you
	# will search for a particular term
	#
	# TODO: ADD 4 LINES OF CODE THAT LOOPS THROUGH metadata.jsonld IN metadata,
	#	CHECKS FOR ocr_simple, AND ADDS THE ocr_simple TEXT TO text_store IF PRESENT
	
	
	

# find the keyword from the ocr results
#
# THIS is where you will search text_store for your search term.
# You should use the search function you created above.
# Note: do this after the loop through the files is finished  
#
# TODO: ADD ONE LINE OF CODE.  MAKE YOUR SEARCH TERM 'information'



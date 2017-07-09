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
	for k in values.keys():
		if searchFor in values[k].lower():
			found.append(k)
	return found

#parameters to access BD services
bds = 'https://bd-api.ncsa.illinois.edu'

# key and token from the Brown Dog API Gateway service
token = ""

# path to the folder to process
input_path = "input"

# create a list of files that is not a folder
onlyfiles = [join(input_path, f) for f in os.listdir(input_path) if isfile(join(input_path, f))]

text_store = {}

# processing the files in the given folder
for (input_file) in onlyfiles:
	filename, file_extension = splitext(basename(input_file))
	input_format = file_extension[1:]

	print 'Processing file: ' + basename(input_file) 
	
	# do the extraction
	metadata = bd.extract(bds, input_file, token, 120)		
	# process the metadata 
	# find the "OCR" results and store
	for m in metadata['metadata.jsonld']:
		txt = findItem(m, 'ocr_text')
		if not (txt is None):
			text_store[basename(input_file)] = txt
# find the keyword from the ocr results
print text_store
print search(text_store, 'information')

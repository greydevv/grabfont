import zipfile
import requests
import os
import sys

def download_font(font_family, out_dir):
	"""
	'download_font' is the entry point for the downloading process.
	
	Parameters
	----------
	'font_family' (str) the font name to download (ex: 'Roboto')
	'out_dir'     (str) the download directory
	
	Returns
	-------
	None

	Errors
	------
	'download_font' itself is not responsible for abnormally
	exiting the program; however, '__get_font_data' and 
	'__verify_dir', both of which are responsible for checking
	a condition and exiting accordingly, are called from this
	function.
	"""
	response = __get_font_data(font_family)

	# if no directory is specified, assume it should be the current working directory
	# resulting directory will end with a directory named <FONT_FAMILY>
	if not out_dir:
		out_dir = os.getcwd()
	out_dir = f"{out_dir}/{font_family}"

	__verify_dir(out_dir)

	print("Writing...")
	# writing the binary data retrieved from 'requests.get' to <FONT_FAMILY>.zip
	out_file = f"{font_family}.zip"
	with open(out_file, "wb") as f: 
		f.write(response.content)

	print("Unzipping...")
	 # extracting files to the /<FONT_FAMILY> directory
	with zipfile.ZipFile(out_file, "r") as zip_ref:
		zip_ref.extractall(out_dir)
	print("Deleting original zip file...")
	# removing the original zip file left after extraction
	os.remove(out_file)

	print(f"All files extracted!\nLocation: {out_dir}")
	sys.exit(0)


def __verify_dir(query_dir):
	"""
	'__verify_dir' checks if a directory already exists. If not,
	the directory is created.

	Parameters
	----------
	'query_dir' (str) the directory to verify

	Returns
	------
	None

	Errors
	------
	The program exits with a non-zero exit code if the folder
	already exists.
	"""
	if os.path.exists(query_dir) and os.path.isdir(query_dir):
		print(f"Error: folder named '{font_family}' already exists.")
		sys.exit(1)
	else:
		os.mkdir(query_dir)
		

def __get_font_data(font_family):
	"""
	'__get_font_data' downloads the specified font family from
	'fonts.google.com' via an HTTP GET request.

	Parameters
	----------
	'font_family' (str) the font name to download (ex: 'Roboto')
	
	Returns
	-------
	'__get_font_data' returns the data retrieved from the HTTP
	GET request.

	Errors
	------
	The program exits with a non-zero exit code if the font
	does not exist.
	"""
	response = requests.get(f"https://fonts.google.com/download?family={font_family}")

	# check for HTTP 404 error (this means the font does not exist on fonts.google.com)
	if response.status_code == 404:
		print(f"Error: '{font_family}' does not exist. Please check your spelling and try again.")
		sys.exit(1)
	return response
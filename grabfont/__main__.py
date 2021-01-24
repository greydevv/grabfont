import argparse
from grabfont.download import download_font

def main():
	"""
	'main' is the main entry point of the console script.
	
	Usage
	-----

	usage: grabfont [-h] font [dir]

	positional arguments:
	  font        The font name to download (ex: 'Roboto')
	  dir         The directory to download the font to.

	optional arguments:
	  -h, --help  show this help message and exit

	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("font", type=str, help="The font name to download (ex: 'Roboto')")
	parser.add_argument("dir", type=str, nargs="?", default=None, help="The directory to download the font to.")

	args = parser.parse_args()
	download_font(args.font.replace(" ", "+"), args.dir)
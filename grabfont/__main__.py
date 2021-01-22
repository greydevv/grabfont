import wget
import zipfile
import os
from urllib.error import HTTPError

def main(font_family, out_dir=os.getcwd(), unzip=False):
	url = f"https://fonts.google.com/download?family={font_family}"

	# dest = f"{dest}/{font_family}"
	if os.path.exists(out_dir):
		print(f"Uh oh, it looks like you already have a folder named '{font_family}'\n{out_dir}")
		return
	else:
		os.mkdir(out_dir)

	try:
		filename = wget.download(url, out=out_dir)
		if unzip:
			unzip_file(filename, out_dir)

		print(f"Success! You can find your font here:\n{out_dir}")
	except HTTPError as e:
		if "HTTP Error 404" in str(e):
			print(f"[Status: 404]\nFont family, '{font_family}', not found.")


def unzip_file(file, out_dir):
	with zipfile.ZipFile(file, 'r') as zip_ref:
		zip_ref.extractall(out_dir)
	os.remove(file)


if __name__ == "__main__":
	font_family = "Lato"
	out_dir = f"{os.getcwd()}/{font_family}"
	main(font_family, out_dir=out_dir, unzip=True)



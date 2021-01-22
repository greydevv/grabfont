from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()


setup(
	name = "grabfont",
	version = "0.1.0",
	author = "Greyson Murray",
	author_email = "greysonmurray.dev@gmail.com",
	description = "Font downloader from fonts.google.com",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/greysonDEV/grabfont",
	license = "MIT",
	classifiers = [
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.8",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Natural Language :: English"
	],
	python_requires=">=3.8",
	install_requires=[
		"wget",
	],
	include_package_data=True,
	packages = ["grabfont"],
	entry_points = {
		"console_scripts": [
			"grabfont = grabfont.__main__:main"
		]
	},
)
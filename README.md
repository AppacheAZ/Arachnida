# Arachnida
This is a 42 Cybersecirity-Bootcamp project.
This project is a webscraping tool to download images from websites and a metadata analyzer.

## Pre-requisites
* Python 2.7 or higher
* beautifulsoup4, to install it run:
<pre><code>pip install beautifulsoup4</code></pre>
* requests, to install it run:
<pre><code>pip install requests</code></pre>
* Pillow, to install it run:
<pre><code>pip install Pillow</code></pre>

## Spider (webscraping)
The spider is a tool to download images from websites. It can be used to download all images from a website or from a list of websites in a recursive way.

### Usage
1 - Clone the repository
<pre><code>git clone https://github.com/AppacheAZ/Arachnida.git Arachnida_repository</code></pre>

2 - Go to the spider directory
<pre><code>cd Arachnida_repository</code></pre>

3 - Run the spider
<pre><code>python3 spider.py [OPTIONS] [URL]</code></pre>
* OPTIONS:
  * -h, --help: Display the help message
  * -r, --recursive_links: Download images from the given URL and from all the links in the given URLS (URL must be provided as an argument)
  * -l, --level: Set the level of recursion (for default: 5) y recomend use 1 or 3, 4 or more can be very slow
  * -p, --path: Set the path where the images will be downloaded (for default: ./images)

## Scorpion (metadata analyzer)
The scorpion is a tool to analyze the EXIF metadata of images. It can be used to analyze the metadata of a single image or of all the images in a directory.
 ### Usage
1 - Clone the repository
<pre><code>git clone https://github.com/AppacheAZ/Arachnida.git Arachnida_repository</code></pre>

2 - Go to the spider directory
<pre><code>cd Arachnida_repository</code></pre>

3 - Run the scorpion
<pre><code>python3 scorpion.py [IMAGE/S...]</code></pre>
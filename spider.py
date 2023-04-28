from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import argparse
import os

def get_images(url):
    url_components = urlparse(url) # Parse the url (analyze and split it)
    url = url if url_components.scheme else url_components._replace(scheme='http').geturl() # If the url doesn't have a scheme, add http

    page_content = requests.get(url) # Get the content of the url
    html = page_content.content # Get the content of the page
    
    soup = BeautifulSoup(html, 'html.parser') # Parse the html

    # Create a directory to save the images if it doesn't exist
    os.makedirs('img_downloads', exist_ok=True)

    print(f"\n \n Downloading images from {url} \n \n")
    for image in soup.find_all('img'):
        image_url = image.get('src')
        if image_url and (image_url.startswith('http') or image_url.startswith('https')): #if the image has a src attribute, complete the url
            full_image_url = urljoin(url, image_url)
            image_content = requests.get(full_image_url) # Get the content of the image
            image_filename = os.path.join('img_downloads', image_url.split('/')[-1]) # Get the filename of the image
            with open(image_filename, 'wb') as f: # Write the image in the directory
                f.write(image_content.content)
            print(f'Image {image_filename} downloaded')

def get_title(url):

    response = requests.get(url)

    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('title').text
    return(title)

def get_links(url):
    url_components = urlparse(url) # Parse the url (analyze and split it)
    url = url if url_components.scheme else url_components._replace(scheme='http').geturl() # If the url doesn't have a scheme, add http

    page_content = requests.get(url) # Get the content of the url
    html = page_content.content # Get the content of the page
    
    soup = BeautifulSoup(html, 'html.parser') # Parse the html

    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('http') or link['href'].startswith('https'): #if the image has a src attribute, complete the url
            full_link_url = urljoin(url, link['href'])
            links.append(full_link_url)
    return links

def recursive_links(url, level):
    links = []

    while level > 0:
        links = get_links(url)
        level -= 1
        for link in links:
            print(link)
            recursive_links(link, level)
    return links

def main():
    parser = argparse.ArgumentParser(description='Process HTML pages')
    parser.add_argument('-d', '--description', action='store_true', help='description of the program')
    parser.add_argument('-t', '--title', action='store_true', help='title of the page')
    parser.add_argument('-r', '--recursive', action='store_true', help='images in the page')
    parser.add_argument('url', help='URL of the page to process')
    parser.add_argument('-l', '--links', action='store_true', help='links in the page')
    parser.add_argument('-k', '--recursive_links', action='store_true', help='links in the page')


    args = parser.parse_args()

    if args.description:
        print('This program will print the title and links of a given URL')
    if args.title:
        print(get_title(args.url))
    if args.recursive:
        print(f'This program will download all images in a given URL in the PATH: {os.getcwd()}')
        get_images(args.url)
    if args.links:
        print(f'This program will print all links in a given URL')
        get_links(args.url)
    if args.recursive_links:
        print(f'This program will print all links in a given URL')
        for i in recursive_links(args.url, 2):
            get_images(i)


if __name__ == '__main__':
    main()
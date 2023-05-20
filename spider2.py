from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import argparse
import os
import time


# PROBLEM: Create a program with a function called 'spider' that recursively extracts all the images from a website.
# The function should receive a url and a path as arguments. The path is the directory where the images will be saved.
# '-r' means that the spider will download the images from the first page.
# '-l 3' means that the spider will go 3 levels deep in the website.


# First parse the url given by the user
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
        else:
            continue          
    return links

# Recursive function that extracts all the links from a website
def recursive_links(url, level):
    visited_links = set()
    links_stack = [url]
    visited_links.add(url)
    while level > 0 and links_stack:
        current_link = links_stack.pop()
        level -= 1
        links = get_links(current_link)
        for link in links:
            print(link)
            if link not in visited_links:
                links_stack.append(link)
                visited_links.add(link)
    return (visited_links)

# Function that extracts the title of a website
def get_title(url):

    response = requests.get(url)

    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('title').text
    return(title)

# Function that extracts all the images from a website
def get_images(url, path):
    url_components = urlparse(url) # Parse the url (analyze and split it)
    url = url if url_components.scheme else url_components._replace(scheme='http').geturl() # If the url doesn't have a scheme, add http
    main_url = url_components.scheme + '://' + url_components.netloc + '/'

    page_content = requests.get(url) # Get the content of the url
    html = page_content.content # Get the content of the page
    
    soup = BeautifulSoup(html, 'html.parser') # Parse the html

    # Create a directory to save the images if it doesn't exist
    os.makedirs(path, exist_ok=True)

    #print(f"\n \n Downloading images from {url} \n \n")

    for image in soup.find_all('img'):
        image_url = image.get('src')
        #print(f"\n \n url original: {image_url}")
        try:
            if image_url and (image_url.startswith('http') or image_url.startswith('https')): #if the image has a src attribute, complete the url
                full_image_url = urljoin(url, image_url)
                print(f"url completo: {full_image_url}")
                image_content = requests.get(full_image_url) # Get the content of the image
                image_filename = os.path.join(path, image_url.split('/')[-1]) # Get the filename of the image
                with open(image_filename, 'wb') as f: # Write the image in the directory
                    f.write(image_content.content)
                print(f'Image {image_filename} downloaded')
            elif image_url:
                full_image_url = urljoin(main_url, image_url)
                print(f"url completo: {full_image_url}")
                image_content = requests.get(full_image_url) # Get the content of the image
                image_filename = os.path.join(path, image_url.split('/')[-1]) # Get the filename of the image
                with open(image_filename, 'wb') as f: # Write the image in the directory
                    f.write(image_content.content)
                #print(f'Image {image_filename} downloaded')
        except Exception as e:
            print(e)
            continue

# Main function where the user can choose the options
def main():
    parser = argparse.ArgumentParser(prog ='Spider', description='Scraping tool to web images', epilog='Arachnida exercise from cybersecurity bootcamp of 42 Urduliz')
    parser.add_argument('-d', '--description', action='store_true', help='description of the program')
    parser.add_argument('-t', '--title', action='store_true', help='title of the page')

    parser.add_argument('-r', '--recursive_links', action='store_true', help='links in the page')
    parser.add_argument('-l', '--level', type=int, default = 5, help='level of recursion')
    parser.add_argument('-p', '--path', default = "./data", help='PATH to save the images')
    
    parser.add_argument('url', help='URL of the page to process')

    args = parser.parse_args()
    

    if args.description:
        print('This program will print the title and links of a given URL')
    if args.title:
        print(get_title(args.url))
    if args.recursive_links:
        print(f'This program will print all links in a given URL')
        start_time = time.time()
        for i in recursive_links(args.url, args.level):
            print(i)
            get_images(i, args.path)
        print(f"--- {(time.time() - start_time)} seconds ---")

if __name__ == '__main__':
    main()
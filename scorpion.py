import  argparse
from PIL import Image
from PIL.ExifTags import TAGS

# PROBLEM: Create a program with a function called 'spider' that analyze images to extract EXIF data 


def main():
        # Create the parser
        parser = argparse.ArgumentParser(
              prog ='Scorpion', description='Metadata image analyzer', 
              epilog='Arachnida exercise from cybersecurity bootcamp of 42 Urduliz'
              )
        parser.add_argument('-d', '--description', action='store_true', help='description of the program')
        parser.add_argument('[IMAGE]', help = 'image to analyze')
        parser.add_argument('[IMAGES]', help='image(s) to analyze', nargs='+')

        args = parser.parse_args()
        if args.description:
            print('This program will print the metadata of a given image')
        if args.help:
            print('Usage:python scorpion.py [-h] [-d] [IMAGE]\n This program extraxt EXIF data from images\n\n' 
                 'positional arguments:\n IMAGE image to analyze\n\n optional arguments:\n -h, --help show this help message and exit\n'
                 '-d, --description description of the program\n'
                 )


if __name__ == '__main__':
    main()
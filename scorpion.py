import  argparse

from PIL import Image
from PIL.ExifTags import TAGS

# PROBLEM: Create a program with a function called 'scorpion' that analyze images 
# Extract EXIF data from the images given by the user
# It must be compatible with the extensions of the spider program

def scorpion(image_paths):
    # Iterate over the paths of the images given by the user
    for image_path in image_paths:
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            if exif_data is not None:
                # Basic info about the image
                print(f"Name: {image.filename.split('/')[-1]}")
                print(f"Size: {image.size}")
                print(f"Format: {image.format}")
                print(f"Mode: {image.mode}")
                print(f"Pallette: {image.palette}")
                print("------------------Exif data found------------------")
                # Iteration of the exif data
                for id, value in exif_data.items():
                    print(f"{TAGS.get(id)}: {value}")
            else:
                print("No Exif data found.")
        
        except Exception as e:
            print(f"Error: {e}")
        print("\n" + "-" * 100 + "\n")



def main():
        # Create the parser to analyze the arguments given by the user
        parser = argparse.ArgumentParser(
              prog ='Scorpion', description='Metadata image analyzer', 
              epilog='Arachnida exercise from cybersecurity bootcamp of 42 Urduliz'
              )
        parser.add_argument('-d', '--description', action='store_true', help='description of the program')
        parser.add_argument('IMAGE', help = 'image to analyze', type=str)
        parser.add_argument('IMAGES', help='image(s) to analyze', type=str, nargs='*')

        args = parser.parse_args()
        if args.description:
            print('This program will print the metadata of a given image')
        if args.IMAGE:
            scorpion([args.IMAGE])
        if args.IMAGES:
            ubication = list()
            ubication.append(args.IMAGE)
            ubication += args.IMAGES
            scorpion(ubication)


if __name__ == '__main__':
    main()
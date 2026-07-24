import os
import sys

def check_and_open_image():
    # 1. CHECK FOR COMMAND LINE ARGUMENT
    # sys.argv is a list of what you typed in the command prompt.
    # sys.argv[0] is the script name. sys.argv[1] will be your pasted path.
    if len(sys.argv) < 2:
        print("Error: You didn't provide an image path.")
        print('Usage: python open_image.py ""C:\Users\jyoth\Downloads\download (1).webp""')
        return

    # Grab the path from the command prompt input
    image_path = sys.argv[1]

    # 2. CHECK IF IT EXISTS
    if os.path.exists(image_path):
        print(f"Success! Image found at: {image_path}")
        print("Opening image now...")
        
        # 3. OPEN THE IMAGE
        # This command tells Windows to open the file with its default program
        os.startfile(image_path)
        
    else:
        print(f"Error: The image does not exist at:")
        print(image_path)
        print("Please double-check the path and try again.")

if __name__ == "__main__":
    check_and_open_image()
import os
from PIL import Image

def change_image_color(input_path, output_path, new_color):
    # Open the image
    image = Image.open(input_path)

    # Create a blank image with the same size and mode as the original image
    colored_image = Image.new("RGBA", image.size)

    # Loop through each pixel of the image
    for x in range(image.width):
        for y in range(image.height):
            # Get the color of the pixel at (x, y)
            pixel_color = image.getpixel((x, y))

            # Check if the pixel is not transparent
            if pixel_color[3] != 0:
                # Create a new color with the specified RGBA values
                new_pixel_color = (new_color[0], new_color[1], new_color[2], pixel_color[3])

                # Set the new color for the pixel in the blank image
                colored_image.putpixel((x, y), new_pixel_color)

    # Save the modified image in the "output" folder
    colored_image.save(output_path)

def process_images(input_folder, output_folder, new_color):
    # Create the "output" folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the files in the "image" folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Process the image and save the modified image in the "output" folder
            change_image_color(input_path, output_path, new_color)

if __name__ == "__main__":
    input_image_folder = "image"  # Folder containing input images
    output_image_folder = "output"  # Folder to store modified images
    new_color = (240, 3, 0)  # RGB values for #F00300 (Red color)

    process_images(input_image_folder, output_image_folder, new_color)
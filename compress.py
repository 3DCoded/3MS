import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder, resolution):
    """
    Resizes all images in a folder to a constant resolution.

    Args:
        folder_path (str): Path to the folder containing images.
        output_folder (str): Path to save the resized images.
        resolution (tuple): Desired resolution (width, height) in pixels.

    Returns:
        None
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        try:
            # Open image
            with Image.open(file_path) as img:
                # Resize image
                img_resized = img.resize(resolution)

                # Save resized image to the output folder
                output_path = os.path.join(output_folder, file_name)
                img_resized.save(output_path)

                print(f"Resized and saved: {output_path}")

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "raw_images"  # Replace with your folder path
    output_folder = "assets/images/instructions"  # Replace with your output folder path
    target_resolution = (2000,1500)  # Replace with your desired resolution (width, height)

    resize_images_in_folder(input_folder, output_folder, target_resolution)


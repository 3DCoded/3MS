import os
from PIL import Image
import secrets

def is_hash(s):
    s = s.split('.')[0]
    return len(s) == 8 and all(c in '0123456789abcdef' for c in s)

def resize_images_in_folder(folder_path, output_folder, width):
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

        if os.path.exists(os.path.join(output_folder, file_name)):
            # print(f'Skipping: {file_name}')
            continue

        try:
            # Open image
            with Image.open(file_path) as img:
                # Resize image
                # img_resized = img.resize((width, ))
                img.thumbnail((2000, 1500))

                # Save resized image to the output folder
                new_file_name = file_name if is_hash(file_name) else secrets.token_hex(4)+'.'+file_name.split('.')[1]
                output_path = os.path.join(output_folder, new_file_name)
                img.save(output_path)
                os.rename(file_path, os.path.join(folder_path, new_file_name))

                # print(f"Resized and saved: {output_path}")
                print(*new_file_name.split('.'))

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "raw_images"  # Replace with your folder path
    output_folder = "docs/assets/images/web"  # Replace with your output folder path
    # target_resolution = (2000,1500)  # Replace with your desired resolution (width, height)

    resize_images_in_folder(input_folder, output_folder, 2000)


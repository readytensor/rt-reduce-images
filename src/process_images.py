import os
from typing import Optional, Tuple

from PIL import Image

import paths


def compress_image(img: Image.Image, quality: int = 85) -> Image.Image:
    """
    Compress an image by reducing its quality.

    Args:
        img: PIL Image object to compress.
        quality: Quality setting for compression (1 to 100).
                 Lower means more compression and smaller file size.

    Returns:
        Compressed PIL Image object.
    """
    # Create a new image in memory
    compressed_img = Image.new(img.mode, img.size)
    compressed_img.paste(img)
    
    # We don't actually save here, just return the image object
    # The quality setting will be used when saving later
    return compressed_img


def resize_image(img: Image.Image, width: int, height: Optional[int] = None) -> Image.Image:
    """
    Resize an image to reduce its file size.

    Args:
        img: PIL Image object to resize.
        width: New width to resize the image to.
        height: New height to resize the image to. If None, aspect ratio will be maintained.

    Returns:
        Resized PIL Image object.
    """
    if height is None:
        # Calculate height to maintain aspect ratio
        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio)
    
    return img.resize((width, height), Image.LANCZOS)


def convert_image_format(img: Image.Image, output_format: str = "JPEG") -> Image.Image:
    """
    Convert an image to a different format to reduce file size.

    Args:
        img: PIL Image object to convert.
        output_format: Format to convert the image to (e.g., "JPEG", "PNG", "WEBP").

    Returns:
        Converted PIL Image object.
    """
    if img.mode != "RGB" and output_format.upper() in ["JPEG", "WEBP"]:
        return img.convert("RGB")
    return img


def run_workflow(
    input_image_path: str,
    output_image_path: str,
    output_format: str = "JPEG",
    width: int = 800,
    height: Optional[int] = None,
    quality: int = 50
) -> None:
    """
    Run the image processing workflow: format conversion, resizing, and compression.

    Args:
        input_image_path: Path to the input image.
        output_image_path: Path to the output image.
        output_format: Format to convert the image to (e.g., "JPEG", "PNG", "WEBP").
        width: New width to resize the image to.
        height: New height to resize the image to. If None, aspect ratio will be maintained.
        quality: Quality setting for compression (1 to 100).

    Returns:
        None
    """
    with Image.open(input_image_path) as img:
        # Convert the image format
        img = convert_image_format(img, output_format)
        
        # Resize the image
        img = resize_image(img, width, height)
        
        # Compress the image
        img = compress_image(img, quality)
        
        # Save the processed image
        img.save(output_image_path, format=output_format, quality=quality, optimize=True)


def process_directory(
    input_directory: str,
    output_directory: str,
    input_format: str = "png",
    output_format: str = "JPEG",
    width: int = 800,
    height: Optional[int] = None,
    quality: int = 50
) -> None:
    """
    Process all images in a directory that match the given format.

    Args:
        input_directory: Directory containing the input images.
        output_directory: Directory to save the processed images.
        input_format: Format of the images to process (e.g., 'png').
        output_format: Format to convert the images to (e.g., "JPEG", "PNG", "WEBP").
        width: New width to resize the images to.
        height: New height to resize the images to. If None, aspect ratio will be maintained.
        quality: Quality setting for compression (1 to 100).

    Returns:
        None
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(f".{input_format.lower()}"):
            input_image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(
                output_directory, f"{os.path.splitext(filename)[0]}.{output_format.lower()}"
            )

            print(f"Processing {input_image_path}...")
            run_workflow(input_image_path, output_image_path, output_format, width, height, quality)

    print("All images processed.")


if __name__ == "__main__":
    group_name = "carousel-dark"

    input_dir = os.path.join(paths.images_dir, "original", group_name)
    output_dir = os.path.join(paths.images_dir, "processed", group_name)

    os.makedirs(output_dir, exist_ok=True)

    process_directory(
        input_dir,
        output_dir,
        input_format="png",
        output_format="webp",
        width=800,
        quality=50
    )
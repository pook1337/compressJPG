from PIL import Image

def compress_jpg(input_path, output_path, max_width=1920, quality=85):
    """
    Compress a JPG image with high resolution and good quality.

    :param input_path: Path to the input JPG image
    :param output_path: Path to save the compressed JPG image
    :param max_width: Maximum width to resize the image (preserving aspect ratio)
    :param quality: JPEG quality (1-95), higher means better quality & larger size
    """
    image = Image.open(input_path)
    width, height = image.size

    # Resize if width is greater than max_width, keep aspect ratio
    if width > max_width:
        new_height = int(max_width * height / width)
        image = image.resize((max_width, new_height), Image.LANCZOS)

    # Save with JPEG compression quality
    image.save(output_path, "JPEG", quality=quality, optimize=True)
    print(f"Compressed image saved to {output_path}")

# Example usage
compress_jpg("input.jpg", "output_compressed.jpg", max_width=1920, quality=85)


# compressJPG

A simple Python tool to compress high-resolution JPG images efficiently while maintaining good image quality. This script resizes images if needed and applies JPEG compression to reduce file size, making it ideal for optimizing photos for web or storage.

---

## Features

- Compress high-resolution JPG images with adjustable quality  
- Optional resizing to limit maximum width while preserving aspect ratio  
- Uses Pillow library for image processing  
- Easy to use and integrate into other projects  

---

## Requirements

- Python 3.6+  
- [`Pillow`](https://pypi.org/project/Pillow/) library for image manipulation  

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pook1337/compressJPG.git
   cd compressJPG
   ```

2. Install dependencies:

   ```
   pip install Pillow
   ```

---

## Usage

Run the compression script `cjpg.py` with your input JPG image and specify the output filename.

Example usage inside `cjpg.py`:

```
from PIL import Image

def compress_jpg(input_path, output_path, max_width=1920, quality=85):
    image = Image.open(input_path)
    width, height = image.size

    if width > max_width:
        new_height = int(max_width * height / width)
        image = image.resize((max_width, new_height), Image.LANCZOS)

    image.save(output_path, "JPEG", quality=quality, optimize=True)
    print(f"Compressed image saved to {output_path}")

if __name__ == "__main__":
    compress_jpg("input.jpg", "output_compressed.jpg")
```

Modify the parameters `max_width` and `quality` as needed to balance image quality and file size.

---

## Notes

- The `quality` parameter ranges from 1 (lowest) to 95 (highest). Values between 75-90 usually provide a good balance.  
- The script preserves the aspect ratio when resizing images.  
- Use this tool to optimize images for faster loading times on websites or to save storage space.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


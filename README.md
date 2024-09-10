# Image Processing Script

This script processes images in a directory, applying format conversion, resizing, and compression.

## Requirements

- Python 3.6+
- Pillow library

## Setup

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/image-processing-script.git
   cd image-processing-script
   ```

2. Set up a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a new folder under the `images/original/` directory for your image group (e.g., `images/original/my_group`).

2. Place your images in the newly created directory.

3. Open the `src/process_images.py` script and update the `group_name` variable:

   ```python
   group_name = "my_group"  # Replace with your folder name
   ```

4. Run the script:

   ```
   python src/process_images.py
   ```

5. Processed images will be saved in a corresponding folder under `images/processed/` (e.g., `images/processed/my_group`).

## Customization

Modify the parameters in the `process_directory` function call at the end of the script to adjust:

- Input/output formats
- Image width
- Compression quality

For example:

```python
process_directory(
    input_dir,
    output_dir,
    input_format="jpg",
    output_format="webp",
    width=1024,
    quality=75
)
```

For more detailed customization, edit the `process_directory` function arguments in the script.

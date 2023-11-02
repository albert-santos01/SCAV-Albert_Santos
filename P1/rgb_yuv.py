import numpy as np
import subprocess

# Exercise 1: 
def rgb_to_yuv(r, g, b):
    """
    Convert RGB values to YUV. JPEG/YUV Color Space

    Args:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).

    Returns:
        tuple: YUV values as (Y, U, V).
    """
    y = 0.299 * r + 0.587 * g + 0.114 * b 
    u = 0.492 * (b - y)
    v = 0.877 * (r - y)
    return y, u, v


def yuv_to_rgb(y, u, v):
    """
    Convert YUV values to RGB.

    Args:
        y (int): Y component (0-255).
        u (int): U component (-128-127).
        v (int): V component (-128-127).

    Returns:
        tuple: RGB values as (R, G, B).
    """
    r = y + 1.13983 * v
    g = y - 0.39465 * u - 0.58060 * v
    b = y + 2.03211 * u
    return int(round(r)), int(round(g)), int(round(b))


# Exercise 2:  Use ffmpeg to resize an image
def resize_image(input_path, output_path, width=None, height=None, quality=3):
    """
    Resize an image using ffmpeg.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to the output image.
        width (int, optional): Output width. If None, the original width is used.
        height (int, optional): Output height. If None, the original height is used.
        quality (int, optional): Output quality (1-31), with 1 being the highest quality.
    """
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path,
        '-q:v', str(quality),
    ]

    if width is not None and height is not None:
        ffmpeg_cmd.extend(['-vf', f'scale={width}:{height}'])
    elif width is not None:
        ffmpeg_cmd.extend(['-vf', f'scale={width}:-1'])
    elif height is not None:
        ffmpeg_cmd.extend(['-vf', f'scale=-1:{height}'])

    ffmpeg_cmd.append(output_path)

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"-------------Image resized and saved to {output_path}-----------------")
    except subprocess.CalledProcessError as e:
        print(f"---------------Error resizing image: {e}----------------")

    
def serpentine(input_path, output_path):
    """
    Read the bytes of a JPEG file in the serpentine order and save to a new file.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to the output image.
    """
    try:
        # Read the bytes of the input image file
        with open(input_path, 'rb') as input_file:
            input_bytes = input_file.read()
        
        # Create a list to store the bytes in serpentine order
        serpentine_bytes = []
        
        # Initialize variables for zigzagging through the image
        width, height = 0, 0
        direction = 1  # 1 for right, -1 for left
        
        # Iterate through the input bytes in zigzag order
        for byte in input_bytes:
            serpentine_bytes.append(byte)
            
            # Check if we've reached the end of a row
            if width == 255 and direction == 1:
                width = 0
                height += 1
                serpentine_bytes.append(0x00)  # Insert a null byte as a separator
            
            # Update width based on direction
            width += direction
            
            # Change direction when reaching the edge
            if width == 0:
                direction = 1
            elif width == 255:
                direction = -1
        
        # Write the serpentine bytes to the output file
        with open(output_path, 'wb') as output_file:
            output_file.write(bytes(serpentine_bytes))
        
        print(f"Serpentine order image saved to {output_path}")
    
    except Exception as e:
        print(f"Error reading in serpentine order: {e}")


    # Exercise 4:   Use ffmpeg to transform the previous image into b/w. Do the hardest compression you can.
def convert_to_bw_and_compress(input_path, output_path):
    """
    Convert an image to black and white and apply maximum compression using ffmpeg.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to the output image.
    """
    try:
        # Use ffmpeg to convert the image to black and white and apply maximum compression
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', 'format=gray',
            '-crf', '51',       # Set the compression level (51 is the maximum)
            '-y',               # Overwrite output file if it exists
            output_path
        ]

        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Image converted to B/W and compressed, saved to {output_path}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error converting to B/W and compressing image: {e}")

#Exercise 5: Create a method which applies a run-length encoding from a series of bytes given.
def rle_encode(data):
    """
    Apply run-length encoding to a series of bytes.

    Args:
        data (bytes): Input data.

    Returns:
        bytes: Output data.
    """
    # Create output data
    output_data = bytearray()
    # Loop over input data
    i = 0
    while i < len(data):
        # Get current byte
        b = data[i]
        # Get next byte
        if i + 1 < len(data):
            b_next = data[i + 1]
        else:
            b_next = None
        # Count number of consecutive bytes
        count = 1
        while b_next == b:
            count += 1
            i += 1
            if i + 1 < len(data):
                b_next = data[i + 1]
            else:
                b_next = None
        # Add byte and count to output data
        output_data.extend([b, count])
        # Increment index
        i += 1
    return output_data


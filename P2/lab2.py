import subprocess
import numpy as np
import sys
sys.path.append('../')
import P1.rgb_yuv as p1
import os

def get_name_input_file(input_path):
    """
    Get the name of the input file.

    Args:
        input_path (str): Path to the input file.

    Returns:
        str: Name of the input file with extension.
    """
    return input_path.split('/')[-1]

def get_path_input_file(input_path):
    """
    Get the path of the input file.

    Args:
        input_path (str): Path to the input file.

    Returns:
        str: Path of the input file.
    """
    try:
        return input_path.split('/')[:-1][1]
    except IndexError as e:
        print("The file should be in the data folder")

def get_path_and_name_input_file(input_path):
    """
    Get the path and name of the input file.

    Args:
        input_path (str): Path to the input file.

    Returns:
        str: name of the input file.
        str: path of the input file.

    """
    return get_name_input_file(input_path), get_path_input_file(input_path)

# Exercise 1:
# Convert a video into a mp2 video file and is able to parse
#the ffmpeg -i BBB.mp2" file and save the video info

def video_to_mp2(input_path, output_path):
    """
    Convert a video to mp2 format using ffmpeg.

    Args:
        input_path (str): Path to the input video.
        output_path (str): Path to the output video.
    """
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path,
        '-q:v', '1',
        '-c:v', 'mpeg2video',
        '-c:a', 'mp2',
        '-f', 'mp2',
        output_path
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"---------------Error converting video to mp2: {e}----------------")
        raise e

    

def parse_video_info(input_path):
    """
    Parse the output of ffmpeg -i input_path and return the video info.

    Args:
        input_path (str): Path to the input video.

    Returns:
        dict: A dictionary containing the video info.
    """
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path
    ]
    ffmpeg_output = None
    ffmpeg_output = subprocess.run(ffmpeg_cmd, capture_output=True)
    # /*try:
    # except subprocess.CalledProcessError as e:
    #     print(f"---------------Error parsing video info: {e}----------------")
    #     raise e
    
    ffmpeg_output = ffmpeg_output.stderr.decode('utf-8')
    video_info = {}
    video_info['filename'] = input_path
    video_info['duration'] = ffmpeg_output.split('Duration: ')[1].split(',')[0]
    video_info['bitrate'] = ffmpeg_output.split('bitrate: ')[1].split(' ')[0]
    video_info['resolution'] = ffmpeg_output.split('Stream #0:0')[1].split(' ')[-1].split(',')[0]
    video_info['codec'] = ffmpeg_output.split('Stream #0:0')[1].split(' ')[-2].split(',')[0]
    return video_info

def print_video_info(video_info):
    """
    Print the video info.

    Args:
        video_info (dict): A dictionary containing the video info.
    """
    print('Filename:', video_info['filename'])
    print('Duration:', video_info['duration'])
    print('Bitrate:', video_info['bitrate'])
    print('Resolution:', video_info['resolution'])
    print('Codec:', video_info['codec'])


def exercise1(input_path, output_path):
    """
    Exercise 1:
    Convert a video into a mp2 video file and is able to parse
    the ffmpeg -i BBB.mp2" file and save the video info

    Args:
        input_path (str): Path to the input video.
        output_path (str): Path to the output video.
    """
    input_filename , path_file = get_path_and_name_input_file(input_path)
    output_filename = get_name_input_file(output_path)
    # change the current working directory to the path of the input file
    os.chdir(path_file)

    if not os.path.isfile(input_filename):
        print(f"Input file {input_filename} does not exist.\n")
        raise FileNotFoundError


    video_to_mp2(input_filename, output_filename)
    input("Press Enter to  parse video info ...")
    video_info = parse_video_info(output_filename)
    print_video_info(video_info)
    print("\n")

#-----------------------------------------------------------------------------------------------------

# Exercise 2:
# Create a method which lets you to use ffmpeg to modify the resolution of a video

def modify_resolution(input_path, resolution):
    """
    Modify the resolution of a video using ffmpeg.

    Args:
        input_path (str): Path to the input video.
        resolution (str): Resolution of the output video.
    """

    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'scale=' + resolution,
        input_path.split('.')[0] + '_' + resolution + '.' + input_path.split('.')[1]
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"---------------Error modifying resolution: {e}----------------")
        raise e

def exercise2(input_path, resolution):
    """
    Exercise 2:
    Create a method which lets you to use ffmpeg to modify the resolution of a video

    Args:
        input_path (str): Path to the input video.
        resolution (str): Resolution of the output video.
    """

    input_filename , path_file = get_path_and_name_input_file(input_path)
    # change the current working directory to the path of the input file
    print(os.getcwd())

    if not os.path.isfile(input_filename):
        print(f"Input file {input_filename} does not exist.")
        raise FileNotFoundError
    
    modify_resolution(input_filename, resolution)

#-----------------------------------------------------------------------------------------------------
# Exercise 3:
# Create a me method which lets you change the chroma subsampling
def modify_chroma_subsampling(input_path, chroma_subsampling):
    """
    Modify the chroma subsampling of a video using ffmpeg.

    Args:
        input_path (str): Path to the input video.
        chroma_subsampling (str): Chroma subsampling of the output video.
    """
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path,
        '-pix_fmt', chroma_subsampling,
        input_path.split('.')[0] + '_' + chroma_subsampling + '.' + input_path.split('.')[1]
        
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"---------------Error modifying chroma subsampling: {e}----------------")
        raise e
 

def exercise3(input_path, chroma_subsampling):
    """
    Exercise 3:
    Create a me method which lets you change the chroma subsampling
    
    Args:
        input_path (str): Path to the input video.
        chroma_subsampling (str): Chroma subsampling of the output video.
    """
    input_filename , path_file = get_path_and_name_input_file(input_path)
    # change the current working directory to the path of the input file
    #os.chdir(path_file)

    if not os.path.isfile(input_filename):
        print(f"Input file {input_filename} does not exist.")
        raise FileNotFoundError

    modify_chroma_subsampling(input_filename, chroma_subsampling)

#-----------------------------------------------------------------------------------------------------
# Exercise 4:
#Create another method which lets you read the
#video info and print at least 5 relevant data from the video

def exercise4(input_path):
    """
    Exercise 4:
    Create another method which lets you read the
    video info and print at least 5 relevant data from the video

    Args:
        input_path (str): Path to the input video.
    """
    input_filename , path_file = get_path_and_name_input_file(input_path)
    # change the current working directory to the path of the input file
    #os.chdir(path_file)

    if not os.path.isfile(input_filename):
        print(f"Input file {input_filename} does not exist.")
        raise FileNotFoundError
    
    video_info = parse_video_info(input_filename)
    print_video_info(video_info)

#-----------------------------------------------------------------------------------------------------
# Exercise 5:
#Remember your script from P1? Learn how to
#inheritate and try to do some interaction with it from the new script

def exercise5(R,G,B):
    """
    Exercise 5:
    From P1, it uses the rgb_to_yuv function.
    Converts RGB values to YUV values.
    
    """
    print(f"RGB values: {R}, {G}, {B}")
    y, u, v = p1.rgb_to_yuv(R, G, B)
    print(f"YUV values: {y}, {u}, {v}")


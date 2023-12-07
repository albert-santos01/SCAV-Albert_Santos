import subprocess
import sys
"""
Same as last process (individual script, which 
method will be inheritated in the main one). This 
time, we need to use ffmpeg to extract the YUV 
histogram and create a new video container, which 
video track will have the histogram displayed.

"""
def histogram_video(video_path):
    """
    This function will extract the histogram from the video
    and creates a new video that has only the histogram
    """
    ext=video_path.split('.')[-1]
    video_path_wo_ext = video_path.split('.'+ ext)[0]
    

    subprocess.run([
        'ffmpeg',
        '-i', video_path,
        '-vf', 'histogram',
        video_path_wo_ext + '_histogram.' + ext,
        '-hide_banner'
    ])
    return video_path_wo_ext + '_histogram.' + ext


def incorporate_histogram(video_path):
    """
    This function will incorporate the histogram
    into the video container
    """
    video_histogram_path = histogram_video(video_path)
    ext=video_path.split('.')[-1]
    video_path_wo_ext = video_path.split('.'+ ext)[0]

    subprocess.run([
        'ffmpeg',
        '-i', video_path,
        '-i', video_histogram_path,
        '-filter_complex', 'overlay=0:0',
        '-map', '0:v',
        '-map', '1:v',
      
        video_path_wo_ext + '_with_histogram.' + ext,
        '-hide_banner'
    ])
    
    return video_path_wo_ext + '_with_histogram.' + ext

    
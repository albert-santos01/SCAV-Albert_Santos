import os
import numpy as np
import subprocess
import sys
sys.path.append('../')
import P2.lab2 as p2


#Exercise 1:
"""
Cut 9 seconds from BBB. Start a Python script
that, with the help from FFMpeg, it will have a
method inside a Class, which will output a video
that will show the macroblocks and the motion
vectors
"""
class VideoAnalyzer:
    def __init__(self, input_path, output_path, start_time=0, duration=9):
        self.input_filename = input_path.split("/")[-1]
        self.dir_path = input_path.split(self.input_filename)[0]
        self.input_filename_no_ext = self.input_filename.split(".")[0]

        self.input_path = input_path
        self.outp_macroblock = output_path
        self.start_time = start_time
        self.duration = duration


    def extract_macroblocks_motion_vectors(self):
        # Use FFMpeg to draw macroblocks and motion vectors
        subprocess.run([
            'ffmpeg',
            '-flags2', '+export_mvs',
            '-i', self.input_path,
            '-ss', str(self.start_time),
            '-vf', 'codecview=mv=pf+bf+bb,drawgrid=w=16:h=16:t=2:c=red@0.5 ',
            '-c:a', 'copy',
            '-t', str(self.duration),
            self.outp_macroblock,
            '-hide_banner'
        ])
    def display_output(self):
        # Display the output video
        subprocess.run(['ffplay', self.outp_macroblock])

    # Exercise 2:
    """
    You’re going to create another method in order
    to create a new BBB container. It will fulfill this
    requirements:
    · Cut BBB into 50 seconds only video.
    · Export BBB(50s) audio as MP3 mono track.
    · Export BBB(50s) audio in MP3 stereo w/ lower
    bitrate
    · Export BBB(50s) audio in AAC codec
    Now package everything in a .mp4 with FFMPEG!!
    """
    def extract_video(self):
        # Extract video from the input video
        subprocess.run([
            'ffmpeg',
            '-i', self.input_path,
            '-ss', str(self.start_time),
            '-t', '50',
            '-c:v', 'copy',
            '-an',
            self.dir_path + self.input_filename_no_ext + '_only_video.mp4',
            '-hide_banner'
        ])
    def extract_audio(self):
        # Extract audio from the video
        print(type(self.input_filename))
        print(self.input_filename)
        subprocess.run([
            'ffmpeg',
            '-i', self.input_path,
            '-ss', str(self.start_time),
            '-vn',
            '-c:a', 'mp3',
            '-t', '50',
            self.dir_path + self.input_filename_no_ext + '_audio.mp3',
            '-hide_banner'
        ])
    def extract_audio_mono(self):
        # Extract mono audio from the video
        subprocess.run([
            'ffmpeg',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio.mp3',
            '-ss', str(self.start_time),
            '-ac', '1',
            '-ab', '320',
            self.dir_path + self.input_filename_no_ext +  '_audio_mono.mp3',
            '-hide_banner'
        ])
    def extract_audio_stereo(self):
        # Extract stereo audio from the video
        subprocess.run([
            'ffmpeg',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio.mp3',
            '-ss', str(self.start_time),
            '-ac', '2',
            '-ab', '96',
            self.dir_path + self.input_filename_no_ext +  '_audio_stereo.mp3',
            '-hide_banner'
        ])

    def extract_audio_aac(self):
        subprocess.run([
            'ffmpeg',
            '-i', self.input_path,
            '-ss', str(self.start_time),  # Start time (in seconds)
            '-t', '50',  # Duration (in seconds)
            '-vn',  # Disable video recording
            '-c:a', 'aac',  # Set audio codec to AAC
            '-b:a', '192k',  # Set audio bitrate (adjust as needed)
            self.dir_path + self.input_filename_no_ext +  '_audio.aac',
            '-hide_banner'
        ])

    #def package(self):





                
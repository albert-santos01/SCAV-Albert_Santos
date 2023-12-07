import os
import numpy as np
import subprocess
import sys
import json
sys.path.append('../')
import P2.lab2 as p2
import P3.subtitles_manager as sm
import P3.histogram_yuv as hyuv
#Exercise 1:
"""
Cut 9 seconds from BBB. Start a Python script
that, with the help from FFMpeg, it will have a
method inside a Class, which will output a video
that will show the macroblocks and the motion
vectors
"""
class VideoAnalyzer:
    def __init__(self, input_path, start_time=0, duration=9):
        self.input_filename = input_path.split("/")[-1]
        self.dir_path = input_path.split(self.input_filename)[0]
        self.input_filename_no_ext = self.input_filename.split(".")[0]

        self.input_path = input_path
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
            self.dir_path + self.input_filename_no_ext + '_macroblock.mp4',
            '-hide_banner'
        ])
    def display_output(self):
        # Display the output video
        subprocess.run(['ffplay', self.dir_path + self.input_filename_no_ext + '_macroblock.mp4', '-hide_banner'])

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
            '-ac', '1',
            '-b:a', '320k',
            self.dir_path + self.input_filename_no_ext +  '_audio_mono.mp3',
            '-hide_banner'
        ])
    def extract_audio_stereo(self):
        # Extract stereo audio from the video
        subprocess.run([
            'ffmpeg',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio.mp3',
            '-ac', '2',
            '-b:a', '96k',
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

    def create_mp4(self):
        # Create the final mp4 file
        subprocess.run([
            'ffmpeg',
            '-i', self.dir_path + self.input_filename_no_ext + '_only_video.mp4',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio_mono.mp3',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio_stereo.mp3',
            '-i', self.dir_path + self.input_filename_no_ext + '_audio.aac',
            '-map', '0:v',
            '-map', '1:a',
            '-map', '2:a',
            '-map', '3:a',
            '-c:v', 'copy',
            '-c:a', 'copy',
            self.dir_path + self.input_filename_no_ext + '_final.mp4',
            '-hide_banner'
        ])
        isdisp=input("Do you want to display the output video? (y/n): ")
        if isdisp == "y":
            subprocess.run(['ffplay', self.dir_path + self.input_filename_no_ext + '_final.mp4', '-hide_banner'])
        else:
            print("The video is saved in the data folder")

    """
    Exercise 3:
    Create another method which reads the tracks 
    from an MP4 container, and it’s able to say how 
    many tracks does the container contains

    """
    def get_tracks_info(self,path):
        # Use FFmpeg to get information about tracks in the MP4 container
        result = subprocess.run([
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'stream=index,codec_type',
            '-of', 'json',
            path
        ], capture_output=True, text=True)

        # Parse the JSON output from FFprobe
        try:
            data = json.loads(result.stdout)
            streams = data.get('streams', [])
            return streams
        except json.JSONDecodeError:
            print("Error decoding JSON output from FFprobe.")
            return None
        
    def count_tracks(self,path=None):
        # Count the number of tracks in the input video
        if path is None:
            path = self.input_path
         # Get information about tracks
        tracks_info = self.get_tracks_info(path)
        


        if tracks_info:
            print("Number of tracks: {}".format(len(tracks_info)))
            n_video_tracks = 0
            n_audio_tracks = 0            
            for track in tracks_info:
                if track['codec_type'] == 'video':
                    n_video_tracks += 1
                elif track['codec_type'] == 'audio':
                    n_audio_tracks += 1
            print("Number of video tracks: {}".format(n_video_tracks))
            print("Number of audio tracks: {}".format(n_audio_tracks))

            
        else:
            print("Unable to retrieve track information.")
    
    def  integrate_subtitles(self):
        # Download the subtitles
        srt_path = sm.download_subtitles(self.input_path)
        # Integrate the subtitles into the video
        output_path_video_with_subtitles = sm.incorporate_subtitles(self.input_path, srt_path)
        # Display the output video
        resp = input("Do you want to display the output video? (y/n): ")
        if resp == "y":
            subprocess.run(['ffplay', output_path_video_with_subtitles, '-hide_banner'])
        else:
            print("The video is saved in the data folder")

    def integrate_histogram(self):
        video_w_histogram = hyuv.incorporate_histogram(self.input_path)
        # Display the output video
        resp = input("Do you want to display the output video? (y/n): ")
        if resp == "y":
            subprocess.run(['ffplay', video_w_histogram, '-hide_banner'])
        else:
            print("The video is saved in the data folder")
    


    





                
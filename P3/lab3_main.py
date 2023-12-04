import os
import numpy as np
import subprocess
from lab3 import VideoAnalyzer
import sys
sys.path.append('../')

if __name__ == '__main__':
    # Go to the central folder
    input_path  = "../data/big_buck_bunny.mp4"
    output_path1 = "../data/output_lab3_macro.mp4"

    print("------------------Lab 3------------------")
    print(" \t Exercise 1: ")
    print("\t\textract_macroblocks_motion_vectors")
    answer = input("Press Enter to continue or write [s] to skip...")
    if not os.path.exists(input_path):
        print("The file should be in the data folder")
        sys.exit()
    video_analyzer     = VideoAnalyzer(input_path, output_path1, start_time = 240)
    if answer != "s":
        flag   = False
        try:
            video_analyzer.extract_macroblocks_motion_vectors()
        except:
            print("There was an error extracting the macroblocks and motion vectors")
            flag = True

        if not flag:
            resp    =  input("Do you want to display the output video? (y/n): ")
            if resp == "y":
                video_analyzer.display_output()
            else:
                print("The video is saved in the data folder")
    else:
        print("Skipping this exercise")
            


    print("\n \t Exercise 2: ")
    answer = input("Press Enter to continue or write [s] to skip...")
    if answer != "s":
        print("\t\textract_video")
        input("Press Enter to continue...")
        video_analyzer.extract_video()
        input("\n\t\textract_audio\nPress Enter to continue...")
        video_analyzer.extract_audio()
        input("\n\t\textract_audio_mono\nPress Enter to continue...")
        video_analyzer.extract_audio_mono()
        print("\n\t\textract_audio_stereo")
        input("Press Enter to continue...")
        video_analyzer.extract_audio_stereo()
        print("\n\t\textract_audio_aac")
        input("Press Enter to continue...")
        video_analyzer.extract_audio_aac()
        print("\n\t\tcreate_mp4")
        input("Press Enter to continue...")
        video_analyzer.create_mp4()
    else:
        print("Skipping this exercise")

    print("\n \t Exercise 3: ")
    answer = input("Press Enter to continue or write [s] to skip...")
    if answer != "s":
        print("\t\tcount_tracks")
        input("Press Enter to continue...")
        video_analyzer.count_tracks("../data/big_buck_bunny_final.mp4")
    else:
        print("Skipping this exercise")



    input("Press Enter to exit...")





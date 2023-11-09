#importss
import numpy as np
import os
import lab2 as p2


if __name__ == '__main__':
    # Go to the central folder
    os.chdir("..")
    input_path  = "/data/Big_Buck_Bunny-720p.mp4"
    output_path = "/data/Big_Buck_Bunny-720p.mpg"

    print("------------------Lab 2------------------")
    print(" \t Exercise 1: ")
    print("\t\tvideo_to_mp2 and parse_video_info")
    p2.exercise1(input_path, output_path)

    print("\n \t Exercise 2: ")
    input("Press Enter to continue...")
    print("\t\tmodify_resolution")
    p2.exercise2(input_path, "720x480")

    print("\n \t Exercise 3: ")
    input("Press Enter to continue...")
    print("\t\tmodify_chroma_subsampling")
    p2.exercise3(input_path, "yuv420p")

    print("\n \t Exercise 4: ")
    input("Press Enter to continue...")
    print("\t\tparse_video_info")
    p2.exercise4(input_path)

    print("\n \t Exercise 5: ")
    input("Press Enter to continue...")
    print("\t\trgb_to_yuv from rgb_yuv.py")
    p2.exercise5(R=0.5, G=0.7, B=0.3)

    

    
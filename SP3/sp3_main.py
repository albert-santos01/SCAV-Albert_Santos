from video_converter import VideoConverter
import compare_videos as compVid
import docker_ffmpeg_container as docker_ffmpeg
import gui_video_processor as gui

if __name__ == '__main__':
    input_path = "../data/sintel_short.mp4"

    converter = VideoConverter(input_path)
    print("------------------Lab 4------------------")
    print(" \t Exercise 1: ")
    print("Creating all videos requested in the exercise")
    response = input("Press Enter to continue or write [s] to skip... ")
    if response != "s":
        # Convert resolutions
        converter.convert_resolution(1280, 720)
        converter.convert_resolution(854, 480)
        converter.convert_resolution(360, 240)
        converter.convert_resolution(160, 120)

        # Convert codecs
        converter.convert_codec('VP9')
        converter.convert_codec('VP8')
        converter.convert_codec('H.265')
        converter.convert_codec('AV1')
    else:
        print("Skipping this exercise")
    
    print("\n \t Exercise 2: ")
    print("\t\tcompare_videos")
    response = input("Press Enter to continue or write [s] to skip... ")
    if response != "s":
        option = input("Do you want to:\n\t1. Create a video with the two videos side by side\n\t2. Display the two videos side by side\n Option[1][2]: ")
        if option == "1":
            compVid.compare_videos(converter.convert_codec('VP9'), converter.convert_codec('H.265'), "../data/compare_videos.mp4")
        elif option == "2":
            compVid.display_2videos(converter.convert_codec('VP9'), converter.convert_codec('H.265'))
    else:
        print("Skipping this exercise")
    
    print("\n \t Exercise 3: ")
    resp = input("Would you like to go to the GUI? (y/n)")
    if resp == "y":
        gui.main()
    else:
        print("Skipping this exercise")
    
    print("\n \t Exercise 4: ")
    print("Using docker to change the resolution of the video")
    response = input("Press Enter to continue or write [s] to skip... ")
    if response != "s":
        docker_ffmpeg.build_docker_image()
        # docker_ffmpeg.run_docker_image()
        docker_ffmpeg.run_ffmpeg_convert_resolution(input_path, 360, 240)
    else:
        print("Skipping this exercise")

    input("Press Enter to exit...")
    
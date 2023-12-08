import subprocess


def compare_videos(video1, video2, output_file):
    

    # Combine videos horizontally
    command = [
        'ffmpeg',
        '-i', video1,
        '-i', video2,
        '-filter_complex', '[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amix[a]',
        '-map', '[v]',
        '-map', '[a]',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        output_file
    ]
    subprocess.run(command)
    response = input("Do you want to display the output video? (y/n): ")
    if response == "y":
        subprocess.run([
            'ffplay',
            output_file
        ])
    else:
        print("The video is saved in the data folder")
    return output_file

def display_2videos(video1, video2):
    command = [
        'ffplay',
        '-i', video1,
        '-i', video2,
        '-filter_complex', '[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amix[a]',
        '-map', '[v]',
        '-map', '[a]',
        '-hide_banner'
    ]
    subprocess.run(command)
    return

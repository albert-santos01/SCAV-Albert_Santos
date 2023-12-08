import subprocess
import os

def build_docker_image():
    if os.getcwd().split("/")[-1] != "SP3":
        raise Exception("You must be in the SP3 folder to run this script")
    
    print("Building docker image...")
    docker_command = [
        "docker", "build", "-t", "ffmpeg-container", "."
    ]
    print("\n-----\n{}\n-----\n".format(docker_command))
    subprocess.run(["docker", "build", "-t", "ffmpeg-container", "."])

def run_docker_image():
    print("Running docker image...")
    subprocess.run(["docker", "run", "-it", "ffmpeg-container"])

def run_ffmpeg_convert_resolution(input_path, width, height):
    print("\nConverting resolution to {}x{} using ffmpeg through docker...".format(width, height))

    input_path = os.path.abspath(input_path)
    ext = input_path.split(".")[-1]
    video_path_wo_ext = input_path.split('.'+ ext)[0]
    input_dir = os.path.abspath("/".join(input_path.split("/")[:-1]))
    input_filename = input_path.split("/")[-1]

    output_path = video_path_wo_ext + '_docker_{}x{}.'.format(width, height) + ext
    output_file = output_path.split("/")[-1] 

    docker_command = [
        "docker", "run", "-it", 
        "-v", "{}:/app".format(input_dir),
        "ffmpeg-container",
        "ffmpeg", "-i", "/app/{}".format(input_filename),
        "-vf", "scale={}:{}".format(width, height),
        "-y",
        "/app/{}".format(output_file)
    ]
    print("\n-----\n{}\n-----\n".format(docker_command))
    subprocess.run(docker_command)
    return output_path

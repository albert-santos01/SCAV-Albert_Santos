import subprocess

class VideoConverter:
    def __init__(self,input_path):
        self.input_path = input_path
        self.dir_path = "/".join(input_path.split("/")[:-1]) + "/"
        self.input_filename = input_path.split("/")[-1]
        self.input_filename_no_ext = self.input_filename.split(".")[0]
        self.ext= self.input_filename.split(".")[-1]

    def conversion(self,conversion_format):
        # Create the output file path
        output_file_path = self.dir_path + self.input_filename_no_ext + "_converted." + conversion_format

        # Convert the video
        print("Converting the video...")
        subprocess.run([
            'ffmpeg',
            '-i', self.input_path,
            '-hide_banner',
            output_file_path
        ])

        return output_file_path
    
    def convert_resolution(self, width, height):
        # Create the output file path
        output_file = self.dir_path + self.input_filename_no_ext + f'_converted_{width}x{height}.{self.ext}'
        command = [
            'ffmpeg',
            '-i', self.input_path,
            '-vf', f'scale={width}:{height}',
            "-y",
            output_file
        ]
        subprocess.run(command)
        return output_file


    def convert_codec(self, codec):
        dict_codecs= {'VP9': 'libvpx-vp9', 'VP8': 'libvpx', 'H.265': 'libx265', 'AV1': 'libaom-av1'}
        dict_codecs_ext = { 'libvpx-vp9': 'webm', 'libvpx': 'webm', 'libx265': 'mp4', 'libaom-av1': 'mkv'}
        if codec not in dict_codecs:
            print("Codec not supported")
            return
        
        output_file = self.dir_path + self.input_filename_no_ext + f'_converted_{codec}.{dict_codecs_ext[dict_codecs[codec]]}'
        command = [
            'ffmpeg',
            '-i', self.input_path,
            '-c:v', dict_codecs[codec],
            "-y",
            output_file
        ]
        subprocess.run(command)
        return output_file
    
    


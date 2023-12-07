import numpy as np
import subprocess
import sys
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File


def download_subtitles(video_path, language = 'eng'):
    '''
    Downloads the subtitles for a given video
    :param video_path: Path to the video
    :param language: Language of the subtitles
    :return: Path to the downloaded subtitles
    '''
    ost = OpenSubtitles()
    ost.login('albert_scav','albertSCAV123$')
    file_name = video_path.split('/')[-1]
    file_name = file_name.split('.')[0]
    
    file = File(video_path)
    subtitles = ost.search_subtitles([{'sublanguageid': language, 'moviehash': file.get_hash(), 'moviebytesize': file.size}])
    if subtitles:
        subtitle = subtitles[1]
        
        ost.download_subtitles([subtitle['IDSubtitleFile']], override_filenames={subtitle['IDSubtitleFile']: file_name+"_subtitles.srt"}, output_directory='../data', extension='srt')
        print("Subtitles downloaded and saved in data folder")
        return '../data/'+file_name+"_subtitles.srt"
    else:
        print("No subtitles found")
        return None

def incorporate_subtitles(video_path, subtitles_path, output_path=None):
    '''
    Incorporates the subtitles into the video
    :param video_path: Path to the video
    :param subtitles_path: Path to the subtitles
    :param output_path: Path to the output video
    :return: Path to the output video
    '''
    if output_path is None:
        ext=video_path.split('.')[-1]
        video_path_wo_ext = video_path.split('.'+ ext)[0]
        output_path = video_path_wo_ext + '_with_subtitles.' + ext
    subprocess.run([
        'ffmpeg',
        '-i', video_path,
        '-vf', 'subtitles='+subtitles_path,
        '-c:a', 'copy',
        '-t', '00:05:00',
        output_path,
        '-hide_banner'
    ])
    print("Subtitles incorporated into the video but only 5 minutes of the video are shown")
    return output_path
    
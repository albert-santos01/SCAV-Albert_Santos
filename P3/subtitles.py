import numpy as np
import subprocess
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File


def download_subtitles(video_path, language = 'spa'):
    '''
    Downloads the subtitles for a given video
    :param video_path: Path to the video
    :param language: Language of the subtitles
    :return: Path to the downloaded subtitles
    '''
    ost = OpenSubtitles()
    ost.login('','')
    file = File(video_path)
    subtitles = ost.search_subtitles([{'sublanguageid': language, 'moviehash': file.get_hash(), 'moviebytesize': file.size}])
    if subtitles:
        subtitle = subtitles[0]
        ost.download_subtitles([subtitle['IDSubtitleFile']], override_filenames={'input': video_path})
        return subtitle['SubFileName']
    else:
        print("No subtitles found")
        return None
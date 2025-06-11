import os
import re

def preguicinha():

    file_list = os.listdir('.')

    video_files = get_video_files(file_list)

    change_srt(video_files, file_list)

    video_types = [".mp4", ".avi", ".mkv"]

def get_video_files(file_list):
    video_files = []

    for file in file_list:
        if file.endswith('.mp4'):
            video_files.append(file)

    return video_files

def change_srt(mp4_list, file_list):
    for video_file in mp4_list:
        video_index = re.search(r'(S\d{2}E\d{2})', video_file).group(1)

        for srt_file in file_list:
            if srt_file.endswith('.srt') and video_index in srt_file:
                os.rename(srt_file, video_file.replace('.mp4', '.srt'))

preguicinha()
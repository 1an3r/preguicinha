from os import listdir, rename
from re import search
from pathlib import Path
from tkinter.filedialog import askdirectory

path = askdirectory()
BASE_PATH = path

video_types = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
    ".mpg", ".mpeg", ".m4v", ".3gp", ".3g2", ".ts", ".mts", ".m2ts",
    ".ogv", ".vob", ".drc", ".mng", ".drp", ".rm", ".rmvb", ".viv",
    ".asf", ".amv", ".divx", ".xvid", ".yuv", ".bik", ".braw", ".cam",
    ".dat", ".dv", ".dvr-ms", ".asf", ".mxf", ".roq", ".nsv", ".svi",
    ".smk", ".swf", ".braw", ".mng", ".ogm"
]

caption_types = [
    ".srt", ".sub", ".ass", ".ssa", ".smi", ".sami", ".vtt",
    ".sbv", ".scc", ".dfxp", ".ttml", ".itt", ".stl", ".ttxt",
    ".usf", ".rt", ".cap", ".ult", ".cin", ".aqt", ".jss"
]

id_rule = r"(S\d{2}E\d{2})"

def main():
    files = listdir(BASE_PATH)
    videos = get_files_by_extension(files, video_types)
    captions = get_files_by_extension(files, caption_types)

    rename_captions(videos, captions)

def get_files_by_extension(files, extensions):
    return [f for f in files if any(f.lower().endswith(ext) for ext in extensions)]

def get_video_id(video):
    return search(id_rule, video).group(1)

def rename_captions(videos, captions):
    for video in videos:
        video_id = get_video_id(video)

        for caption in captions:
            if video_id in caption:
                new_caption_name = f"{BASE_PATH}\\{video}".replace(Path(video).suffix, Path(caption).suffix)
                current_caption_name = f"{BASE_PATH}\\{caption}"
                rename(current_caption_name, new_caption_name)

main()
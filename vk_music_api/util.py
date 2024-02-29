import re

def get_audio_id_by_link(link: str):
    if data := re.fullmatch(r"https://vk.com/audio([0-9-_]+)", link):
        return data.group(1)
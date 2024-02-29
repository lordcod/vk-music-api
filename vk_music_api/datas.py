from .coonector import Requsts

class Track:
    def __init__(self, requsts: Requsts, data: dict) -> None:
        self.requsts = requsts
        self.data = data
        self.artist_names = data.get("artist")
        self.id = data.get("id")
        self.owner_id = data.get("owner_id")
        self.title = data.get("title")
        self.duration = data.get("duration")
        self.track_code = data.get("track_code")
        self.url = data.get("url")
        self.date = data.get("date")
        self.release_audio_id = data.get("release_audio_id")
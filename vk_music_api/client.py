from .coonector import Requsts
from typing import Optional, Union
from .util import get_audio_id_by_link
from .datas import Track

class Client:
    def __init__(
        self, 
        access_token: str,
        user_agent: str, 
        requsts: Optional[Requsts] = None
    ) -> None:
        self.requsts = requsts or Requsts()
        self.base_url = self.requsts.base_url
        self.requsts.set_authorization(access_token)
        self.requsts.set_user_agent(user_agent)
    
    async def search(self, query: str):
        url = f"{self.base_url}search"
        data = {'q': query}
        track_data = await self.requsts.read_json(url, data=data)
        if 'response' not in track_data:
            return None
        return [Track(self.requsts, dtrack) for dtrack in track_data['response']['items']]
    
    
    async def get_by_ids(self, audio_ids: Union[list, str]):
        url = f"{self.base_url}getById"
        data = {"audios": audio_ids}
        respose = await self.requsts.read_json(url, data=data)
        if 'response' not in respose:
            return None
        return [Track(self.requsts, dtrack) for dtrack in respose['response']['items']]
    
    def get_by_link(self, link: str):
        audio_id = get_audio_id_by_link(link)
        return self.get_by_ids(audio_id)

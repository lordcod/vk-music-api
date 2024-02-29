import aiohttp
import orjson
from aiohttp.client import ClientResponse
from typing import Optional, Mapping, Any, Coroutine

class Requsts:
    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self.datas = {"https": 1,
                      "lang": "en",
                      "extended": 1,
                      "v": 5.131}
        self.headers = {}
        self.session = session
        self.base_url = "https://api.vk.com/method/audio."
    
    async def request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Mapping[str, str]] = None,
        data: Any = None,
        json: Any = None,
        cookies: Optional[Mapping[str, str]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Coroutine[Any, Any, ClientResponse]:
        data = self.get_datas(data)
        headers = self.get_headers(headers)
        if self.session is None:
            async with aiohttp.ClientSession() as session:
                responce = await session.request(
                    method=method, 
                    url=url, 
                    params=params, 
                    data=data, 
                    json=json, 
                    cookies=cookies, 
                    headers=headers
                )
        else:
            responce = await self.session.request(
                method=method, 
                url=url, 
                params=params, 
                data=data, 
                json=json, 
                cookies=cookies, 
                headers=headers
            )
        return responce

    def get(
        self, 
        url: str, 
        **kwargs
    ) -> Coroutine[Any, Any, ClientResponse]:
        method = "GET"
        return self.request(method, url, **kwargs)
    
    def post(
        self, 
        url: str, 
        **kwargs
    ) -> Coroutine[Any, Any, ClientResponse]:
        method = "POST"
        return self.request(method, url, **kwargs)
    
    async def de_json(self, responce: ClientResponse):
        content = await responce.read()
        self
        return orjson.loads(content)
    
    async def read(
        self, 
        url: str, 
        **kwargs
    ) -> str:
        response = await self.post(url, **kwargs)
        data_bytes = await response.read()
        text = data_bytes.decode()
        await self.close_response(response)
        return text
    
    async def read_json(
        self, 
        url: str, 
        **kwargs
    ) -> dict:
        response = await self.post(url, **kwargs)
        data = await self.de_json(response)
        await self.close_response(response)
        return data
    
    async def close_response(self, response: ClientResponse):
        response.release()
        response.close()
    
    def set_authorization(self, token: str) -> None:
        self.datas.update({'access_token': token})

    def set_user_agent(self, user_agent: str) -> None:
        self.headers.update({'User-Agent': user_agent})
    
    def get_datas(
        self, 
        params: Optional[Mapping[str, str]] = None
    ) -> Mapping[str, str]:
        if params is None:
            return self.datas
        params.update(self.datas)
        return params
    
    def get_headers(
        self, 
        headers: Optional[Mapping[str, str]] = None
    ) -> Mapping[str, str]:
        if headers is None:
            return self.headers
        return headers.update(self.headers)
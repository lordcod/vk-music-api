from vk_music_api import Client
from vk_music_api.coonector import Requsts
import os
import asyncio
import aiohttp
from dotenv import load_dotenv

load_dotenv("C:/Users/2008d/git/vk-music-api/.env")

token = os.environ.get('vk_api_token')
agent = os.environ.get('user_agent_api_token')

async def main():
    ses = aiohttp.ClientSession()
    reqs = Requsts(ses)
    print("Start")
    client = Client(token, agent, reqs)
    print("Load client")
    data = await client.search("We Should Plant a Tree")
    print(data[0].data)
    await ses.close()

if __name__ == "__main__":
    asyncio.run(main())

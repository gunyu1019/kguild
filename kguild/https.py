"""MIT License

Copyright (c) 2021 gunyu1019

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import asyncio

import aiohttp

from kguild.api import Api
from models import Vote


class HttpClient:
    """ KoreanBots의 Http 클라이언트를 선언합니다.
     이 클래스를 통하여 KoreanBots API에 연결됩니다.

    Parameters
    ----------
    token: Optional[str]
        KoreanBots 에서 발급받은 서버의 토큰 키값 입니다. 일부 데이터를 반영하거나 불러올 때 토큰 값이 사용될 수 있습니다.
    guild_id: discord.Guild
        디스코드 서버 ID 값이 포함됩니다.
    session: Optional[aiohttp.ClientSession]
        HttpClient 를 위한 aiohttp 의 ClientSession 클래스 입니다.
        기본값은 None이며, 자동으로 ClientSession을 생성하게 됩니다.
    loop: Optional[asyncio.AbstractEventLoop]
        비동기를 사용하기 위한 asyncio.AbstractEventLoop 입니다.
        기본값은 None 입니다.
        기본 asyncio.AbstractEventLoop는 asyncio.get_event_loop()를 사용하여 얻습니다.
    """
    def __init__(self,
                 guild_id: int,
                 token: str = None,
                 session: aiohttp.ClientSession = None,
                 loop: asyncio.AbstractEventLoop = None):
        self.guild_id: int = guild_id
        self.token = token
        self.loop = loop
        self.requests = Api(token=token, session=session, loop=loop)
        self.session = session

    async def vote(self, user_id: int) -> Vote:
        """
        본 함수는 코루틴(비동기)함수 입니다.

        `user_id`에 들어있는 사용자가 서버에 하트를 누른 여부에 대하여 불러옵니다.

        Parameters
        ----------
        user_id: int
            유저 ID 값이 포함되어 있습니다.

        Returns
        -------
        Vote:
            KoreanBots로 부터 들어온 사용자 투표 정보에 대한 정보가 포함되어 있습니다.
        """
        data = {
            "userID": str(user_id)
        }
        path = "/servers/{guild_id}/vote".format(guild_id=self.guild_id)

        self.requests.version = 2
        result = await self.requests.get(path=path, query=data)
        return Vote(result)

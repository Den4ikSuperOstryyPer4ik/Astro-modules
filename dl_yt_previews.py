"""
               _             __  __           _       _
     /\       | |           |  \/  |         | |     | |
    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
 /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/

               © Copyright 2022

      https://t.me/Den4ikSuperOstryyPer4ik
                      and
             https://t.me/ToXicUse

       🔒 Licensed under the GNU AGPLv3
    https://www.gnu.org/licenses/agpl-3.0.html
"""
# meta developer: @AstroModules
# scope: hikka_only
# scope: hikka_min 1.3.0

#imports:
from telethon.tl.types import Message
from .. import loader, utils
from ..inline.types import InlineCall

#module class:
class YTPreviewMod(loader.Module):
    '''Скачивает превью с ютуба'''
    
    #strings en:
    strings = {
        "name": "YT-Preview",
        "choice": '<b>Select YouTube preview extension:</b>',
        "caption": "<b>You have selected an extension: {}</b>",
        "error": "There doesn't seem to be an extension for this video...Choose another.",
    }

    #strings ru:
    strings_ru = {
        "choice": '<b>Выберите расширение для превью ролика YouTube:</b>',
        "caption": "<b>Вы выбрали расширение: {}</b>",
        "error": "Кажется этого расширения для этого видео нету...Выберите другое.",
    }

    #command `.ytp`:
    @loader.command(ru_doc="<link> --> скачивает превью")
    async def ytpcmd(self, message: Message):
        """<link> --> download YouTube video preview"""
        self.args = utils.get_args_raw(message)
        self.chat_id = message.chat_id
        await self.inline.form(
            text=self.strings("choice"),
            reply_markup=[
                [
                    {
                        "text": "maxresdefault",
                        "callback": self.maxresdefault
                    },
                    {
                        "text": "sddefault",
                        "callback": self.sddefault
                    },
                ],
                [
                    {
                        "text": "hqdefault",
                        "callback": self.hqdefault
                    },
                    {
                        "text": "mqdefault",
                        "callback": self.mqdefault
                    },
                ],
                [
                    {
                        "text": "default",
                        "callback": self.default
                    },
                ]
            ],
            message=message
        )

    #callback_handler for button `maxresdefault`:
    async def maxresdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = f"/maxresdefault.jpg"
            count = "maxresdefault"
            nm = self.args.split("=")
            if len(nm) == 2:
                preview = nm[1]
                yt = count1 + preview + count2
            else:
                x = self.args.split("/")
                preview = x[3]
                yt = count1 + preview + count2

            await self._client.send_file(self.chat_id, file=yt, caption=self.strings("caption").format(count))
        except:
            await call.answer(self.strings("error"))

    async def sddefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = f"/sddefault.jpg"
            count = "sddefault"
            nm = self.args.split("=")
            if len(nm) == 2:
                preview = nm[1]
                yt = count1 + preview + count2
            else:
                x = self.args.split("/")
                preview = x[3]
                yt = count1 + preview + count2

            await self._client.send_file(self.chat_id, file=yt, caption=self.strings("caption").format(count))
        except:
            await call.answer(self.strings("error"))

    async def hqdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = f"/hqdefault.jpg"
            count = "hqdefault"
            nm = self.args.split("=")
            if len(nm) == 2:
                preview = nm[1]
                yt = count1 + preview + count2
            else:
                x = self.args.split("/")
                preview = x[3]
                yt = count1 + preview + count2

            await self._client.send_file(self.chat_id, file=yt, caption=self.strings("caption").format(count))
        except:
            await call.answer(self.strings("error"))

    async def mqdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = f"/mqdefault.jpg"
            count = "mqdefault"
            nm = self.args.split("=")
            if len(nm) == 2:
                preview = nm[1]
                yt = count1 + preview + count2
            else:
                x = self.args.split("/")
                preview = x[3]
                yt = count1 + preview + count2

            await self._client.send_file(self.chat_id, file=yt, caption=self.strings("caption").format(count))
        except:
            await call.answer(self.strings("error"))

    async def default(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = f"/default.jpg"
            count = "default"
            nm = self.args.split("=")
            if len(nm) == 2:
                preview = nm[1]
                yt = count1 + preview + count2
            else:
                x = self.args.split("/")
                preview = x[3]
                yt = count1 + preview + count2

            await self._client.send_file(self.chat_id, file=yt, caption=self.strings("caption").format(count))
        except:
            await call.answer(self.strings("error"))
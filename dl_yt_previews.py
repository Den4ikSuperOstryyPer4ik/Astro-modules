# 	
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
# 	
#                                             © Copyright 2024
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/YouTubePreviews.jpg

from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall


class YTPreviewMod(loader.Module):
    '''Скачивает превью с ютуба'''
    
    strings = {
        "name": "YT-Preview",
        "choice": '<b>Select YouTube preview extension:</b>',
        "caption": "<b>You have selected an extension: {}</b>",
        "error": "There doesn't seem to be an extension for this video...Choose another.",
    }

    strings_ru = {
        "choice": '<b>Выберите расширение для превью ролика YouTube:</b>',
        "caption": "<b>Вы выбрали расширение: {}</b>",
        "error": "Кажется этого расширения для этого видео нету...Выберите другое.",
    }

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

    async def maxresdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = "/maxresdefault.jpg"
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
        except Exception:
            await call.answer(self.strings("error"))

    async def sddefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = "/sddefault.jpg"
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
        except Exception:
            await call.answer(self.strings("error"))

    async def hqdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = "/hqdefault.jpg"
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
        except Exception:
            await call.answer(self.strings("error"))

    async def mqdefault(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = "/mqdefault.jpg"
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
        except Exception:
            await call.answer(self.strings("error"))

    async def default(self, call: InlineCall):
        try:
            count1 = "http://i1.ytimg.com/vi/"
            count2 = "/default.jpg"
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
        except Exception:
            await call.answer(self.strings("error"))
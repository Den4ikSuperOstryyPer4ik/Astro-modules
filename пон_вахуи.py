#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @AstroModules
# scope: hikka_only
# scope: hikka_min 1.3.0

import random
from ..inline.types import InlineCall
from telethon.tl.types import Message
from .. import loader

@loader.tds
class ПонВахуиMod(loader.Module):
    """пон и вахуи"""

    strings = {"name": "ПОН-ВАХУИ"}

    @loader.command()
    async def понcmd(self, message: Message):
        """--> инлайн пон"""
        self.chat_id = message.chat_id
        self.reply_pon = await message.get_reply_message()
        await self.inline.form(
            message=message,
            text="👇<b>пон</b>👇",
            reply_markup=[[{"text": "пон", "callback": self.pon}]],
        )

    async def sticker_pon(self, *_):
        m = random.choice(await self._client.get_messages("@PON_STICKS", limit=100))
        if self.reply_pon:
            await self.client.send_message(self.chat_id, file=m, reply_to=self.reply_pon)
        else:
            await self.client.send_message(self.chat_id, file=m)

    async def sticker_vahui(self, *_):
        m = random.choice(await self._client.get_messages("@VAHUI_STICKS", limit=100))
        if self.reply_vahui:
            await self.client.send_message(self.chat_id, file=m, reply_to=self.reply_vahui)
        else:
            await self.client.send_message(self.chat_id, file=m)

    async def pon(self, call: InlineCall):
        await call.edit(
            text="<b>пон</b>",
            reply_markup=[
                [
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                ],
                [
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                ],
                [
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                    {"text": "пон", "callback": self.sticker_pon},
                ],
            ],
        )

    @loader.command()
    async def вахуиcmd(self, message: Message):
        """--> вахуи"""
        self.reply_vahui = await message.get_reply_message()
        self.chat_id = message.chat_id
        await self.inline.form(
            message=message,
            text="👇<b>вахуи</b>👇",
            reply_markup=[[{"text": "вахуи", "callback": self.vahui}]],
        )

    async def vahui(self, call: InlineCall):
        await call.edit(
            text="<b>вахуи</b>",
            reply_markup=[
                [
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                ],
                [
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                ],
                [
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                    {"text": "вахуи", "callback": self.sticker_vahui},
                ],
            ],
        )

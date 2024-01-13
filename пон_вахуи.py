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

import random
import typing

from .. import loader


@loader.tds
class ПонВахуиMod(loader.Module):
    '''пон и вахуи'''

    strings = {"name": "ПОН-ВАХУИ"}

    @loader.command()
    async def пон(self, message):
        """--> инлайн меню со стикерами пон"""
        reply = await message.get_reply_message()
        
        await self.inline.form(
            message=message,
            text="👇<b>пон</b>👇",
            reply_markup=[
                [
                    {
                        "text": "пон",
                        "callback": self.open_menu_pon,
                        "kwargs": {"chat_id": message.chat_id, "reply_to": reply.id if reply else None}
                    }
                ]
            ],
        )
    
    @loader.command()
    async def вахуи(self, message):
        """--> инлайн меню со стикерами "вахуи" """
        reply = await message.get_reply_message()
        
        await self.inline.form(
            message=message,
            text="👇<b>вахуи</b>👇",
            reply_markup=[
                [
                    {
                        "text": "вахуи",
                        "callback": self.open_menu_vahui,
                        "kwargs": {"chat_id": message.chat_id, "reply_to": reply.id if reply else None}
                    }
                ]
            ],
        )

    async def send_sticker_pon(self, chat_id, reply_to: typing.Optional[int] = None):
        m = await self.client.get_messages("@PON_STICKS", ids=random.randint(1, 100))
        await self.client.send_message(chat_id, file=m, reply_to=reply_to)

    async def send_sticker_vahui(self, chat_id, reply_to: typing.Optional[int] = None):
        m = await self.client.get_messages("@VAHUI_STICKS", ids=random.randint(1, 100))
        await self.client.send_message(chat_id, file=m, reply_to=reply_to)

    async def open_menu_pon(self, call, chat_id, reply_to: typing.Optional[int] = None):
        await call.edit(
            text="<b>пон</b>",
            reply_markup=[
                [
                    {"text": "пон", "callback": self.send_sticker_pon, "kwargs": {"chat_id": chat_id, "reply_to": reply_to}}
                    for __ in range(7)
                ]
                for _ in range(3)
            ],
        )
    
    async def open_menu_vahui(self, call):
        await call.edit(
            text="<b>вахуи</b>",
            reply_markup=[
                [
                    {"text": "вахуи", "callback": self.send_sticker_vahui, "kwargs": {"chat_id": chat_id, "reply_to": reply_to}}
                    for __ in range(7)
                ]
                for _ in range(3)
            ],
        )

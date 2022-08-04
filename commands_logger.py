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
#
# meta developer: @AstroModules
# meta pic: https://0x0.st/oeWa.jpg
# meta banner: https://0x0.st/oeW2.png
# scope: hikka_only
# scope: hikka_min 1.3.0

from tokenize import group
from .. import loader, utils as u
import logging
from telethon.tl.functions.channels import InviteToChannelRequest
logger = logging.getLogger(__name__)

@loader.tds
class HikkaCommandsLoggerMod(loader.Module):
    """Hikka Commands Logger"""
    strings = {
        "name": "HikkaCommandsLogger",
        "log-groups": "<b>#GROUP\nCommand:\n« <code>{}</code> »\n\nFrom --> {}\nIn {}\nCommand Message Link --> <a href='https://t.me/c/{}/{}'>CLICK</a></b>",
        "log-pm": "<b>#PM\nCommand:\n« <code>{}</code> »\n\nFrom --> {}</b>",
    }

    async def client_ready(self, client, db):
        logger.warning('Hikka Commangs Logging installed!')
        self.chat_l, _ = await u.asset_channel(
            self.client,
            "hikka-commands-logs",
            "💬 Chat for Hikka Commands LOGGER :) 🔳",
            silent=True,
            avatar="https://0x0.st/oep0.jpg",
        )

        self.chat_logs = f"-100{self.chat_l.id}"
        logger.info("Привет от t.me/AstroModules :)")

    @loader.watcher()
    @loader.tag(only_commands=True)
    async def watcher_chats(self, message):
        sender = await message.get_sender()

        if not sender.username:
            user_link = f"<a href=tg://user?id={sender.id}>{sender.first_name}</a>"
        else:
            user_link = f"<a href='https://t.me/{sender.username}'>{sender.first_name}</a>"

        chat = await self._client.get_entity(message.peer_id)
        chat_title = chat.title
        if not chat.username:
            chat_link = f"{chat_title}"
        else:
            chat_link = f"CHAT: <a href='https://t.me/{chat.username}'>{chat_title}</a>"
        
        async def send():
            await self.inline.bot.send_message(
                self.chat_logs,
                self.strings("log-groups").format(
                    message.raw_text,
                    user_link,
                    chat_link,
                    chat.id,
                    message.id
                ),
                disable_web_page_preview=True,
                parse_mode="HTML",
            )

        try:
            await send()
        except Exception:
            await self._client(
                InviteToChannelRequest(
                    self.chat_l,
                    [self.inline.bot_username],
                )
            )
            await send()

    @loader.watcher()
    @loader.tag(only_commands=True, only_pm=True)
    async def watcher_pm(self, message):
        sender = await message.get_sender()

        if not sender.username:
            user_link = f"<a href=tg://user?id={sender.id}>{sender.first_name}</a>"
        else:
            user_link = f"<a href='https://t.me/{sender.username}'>{sender.first_name}</a>"
        
        async def send():
            await self.inline.bot.send_message(
                self.chat_logs,
                self.strings("log-pm").format(
                    message.raw_text,
                    user_link
                ),
                disable_web_page_preview=True,
                parse_mode="HTML",
            )

        try:
            await send()
        except Exception:
            await self._client(
                InviteToChannelRequest(
                    self.chat_l,
                    [self.inline.bot_username],
                )
            )
            await send()
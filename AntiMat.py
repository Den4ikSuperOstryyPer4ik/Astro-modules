__version__ = (1, 3, 0)
#                _             __  __           _       _
#      /\       | |           |  \/  |         | |     | |
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#                         © Copyright 2022
#
#                https://t.me/Den4ikSuperOstryyPer4ik
#                              and
#                      https://t.me/ToXicUse
#
#                 🔒 Licensed under the GNU AGPLv3
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
from .. import loader, utils
from telethon.tl.types import Message


class AntiMatMod(loader.Module):
    '''Будьте культурным человеком, не материтесь'''

    strings = {
        "name": "Анти-Мат",
        "am_on": "🤬 <b>Антимат включен.</b>",
        "am_off": "🤬 <b>Антимат отключен.</b>",
        "action_text": "Какое действие выполнять при обнаружении мата в сообщении?",
        "list_txt": "Здесь вы можете добавить свои маты.\np.s.: добавляйте по одному мату",
        "added": "<b><emoji document_id=5030749344752468962>➕</emoji> Чат успешно добавлен в антимат систему</b>",
        "uadded": "<b><emoji document_id=5033287275287413303>🗑</emoji> Чат успешно удален из системы антимат</b>",
    }

    async def client_ready(self):
        self.chats = self.get("active", [])

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "list",
                "хер, хрен, хуй, пизда, бля, пох, еблан, еба, шлюха, сука, уебан, пздц, пиздец, пиздос, хую, долбоеб, пидор, гандон, хуя",
                doc=lambda: self.strings("list_txt"),
                validator=loader.validators.Series()
            ),
        )

    @loader.command()
    async def antimat(self, message: Message):
        '''- активировать или диактивировать АнтиМат'''
        antimat = self.db.get(
            "am_status",
            "antimat",
        )
        if antimat == "":
            self.db.set("am_status", "antimat", False)
        if antimat == False:
            self.db.set("am_status", "antimat", True)
            await utils.answer(message, self.strings("am_on"))
        else:
            self.db.set("am_status", "antimat", False)
            await utils.answer(message, self.strings("am_off"))

    @loader.command()
    async def matlist(self, message: Message):
        """- открыть список матов"""
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config Анти-Мат")
        )

    @loader.command()
    async def amaddcmd(self, message: Message):
        """- запретить чату выражаться цензурой"""
        amc = str(utils.get_chat_id(message))

        if amc in self.chats:
            self.chats.remove(amc)
            await utils.answer(message, self.strings("uadded"))
        else:
            self.chats += [amc]
            await utils.answer(message, self.strings("added"))

        self.set("active", self.chats)

    @loader.watcher()
    async def watcher(self, message: Message):
        cid = str(utils.get_chat_id(message))

        txt = message.text
        antimat = self.db.get(
            "am_status",
            "antimat",
        )
        mats = self.config['list']

        if antimat == False:
            return
        if antimat == True:
            if cid not in self.chats:
                for mat in mats:
                    m = txt.lower().find(mat)
                    if m != -1:
                        await message.edit("<emoji document_id=5213285132709929474>🤬</emoji> <b>Не матерись!</b>")
            else:
                for mat in mats:
                    m = txt.lower().find(mat)
                    if m != -1:
                        await utils.answer(message, "<emoji document_id=5213285132709929474>🤬</emoji> <b>Не матерись!</b>")

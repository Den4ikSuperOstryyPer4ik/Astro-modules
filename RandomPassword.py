# ______                 ___  _  _     _____                            _____       _                       ______                ___  _  _
# |  _  \               /   |(_)| |   /  ___|                          |  _  |     | |                      | ___ \              /   |(_)| |
# | | | |  ___  _ __   / /| | _ | | __\ `--.  _   _  _ __    ___  _ __ | | | | ___ | |_  _ __  _   _  _   _ | |_/ /  ___  _ __  / /| | _ | | __
# | | | | / _ \| '_ \ / /_| || || |/ / `--. \| | | || '_ \  / _ \| '__|| | | |/ __|| __|| '__|| | | || | | ||  __/  / _ \| '__|/ /_| || || |/ /
# | |/ / |  __/| | | |\___  || ||   < /\__/ /| |_| || |_) ||  __/| |   \ \_/ /\__ \| |_ | |   | |_| || |_| || |    |  __/| |   \___  || ||   <
# |___/   \___||_| |_|    |_/|_||_|\_\\____/  \__,_|| .__/  \___||_|    \___/ |___/ \__||_|    \__, | \__, |\_|     \___||_|       |_/|_||_|\_\
#                             _                     | |                                         __/ |  __/ |
#                            | |                    |_|                                        |___/  |___/
#            __ _  _ __    __| |
#           / _` || '_ \  / _` |
#          | (_| || | | || (_| |
#           \__,_||_| |_| \__,_|
#  _____                                     ___  _  _
# |_   _|                                   /   |(_)| |
#   | |    ___  __  __ _   _   __ _  _ __  / /| | _ | | __
#   | |   / _ \ \ \/ /| | | | / _` || '__|/ /_| || || |/ /
#   | |  | (_) | >  < | |_| || (_| || |   \___  || ||   <
#   \_/   \___/ /_/\_\ \__, | \__,_||_|       |_/|_||_|\_\
#                       __/ |
#                      |___/
#
#                © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#           https://t.me/ToXicUse
#        🔒 Licensed under the GNU GPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
# scope: hikka_only
# meta developer: @Den4ikSOP_ToXicUse_Mods

import random
from .. import loader, utils
from telethon.tl.types import Message
import asyncio
@loader.tds
class RandomGeneratePasswordMod(loader.Module):
    """Генератор рандомного пароля
    Настроить генератор можно через конфиг
    Авторы: @Den4ikSuperOstryyPer4ik и @ToXicUse"""

    strings = {
        "name": "RandomPasswordGenerator",
        "_cfg_pass_length": "set password length (in number of characters)",
        "_cfg_simbols_in_pass": "",

    }
    strings_ru = {
        "_cfg_pass_length": "выставьте длину пароля(в кол-ве символов)",
        "_cfg_simbols_in_pass": "будут ли в сгенерированном пароле дополнительные символы(+-*!&$#?=@<>)?",
    }

    async def rpgcfgcmd(self, message: Message):
        """—>конфиг этого модуля"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "password length",
                10,
                doc=lambda: self.strings("_cfg_pass_length"),
                validator=loader.validators.Integer(minimum=8),
            ),
            loader.ConfigValue(
                "additional symbols in pass",
                "True",
                doc=lambda: self.strings("_cfg_simbols_in_pass"),
                validator=loader.validators.Boolean(),
            )
        )
    async def generatepasscmd(self, message: Message):
        """—>сгенерировать случайный пароль"""
        await utils.answer(message, '<em>Ваш новый случайный пароль генерируется...</em>')
        await asyncio.sleep(1)
        additional_symbols = self.config["additional symbols in pass"]
        password_length = self.config["password length"]
        if additional_symbols == "True":
            chars = '+-*!&$?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            length = int(self.config["password length"])
            password = ''
            for i in range(length):
                password += random.choice(chars)
                await utils.answer(message, f'<b>Ваш новый сгенерированный пароль в {password_length} символов:</b> <code>{password}</code>')
        else:
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            length = int(self.config["password length"])
            password = ''
            for i in range(length):
                password += random.choice(chars)
                await utils.answer(message, f'<b>Ваш новый сгенерированный пароль в {password_length} символов:</b> <code>{password}</code>')
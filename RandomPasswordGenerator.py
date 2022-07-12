#     ___  ___  ___  ___                    
#    |   \/ __|/ _ \| _ \                   
#    | |) \__ \ (_) |  _/                   
#    |___/|___/\___/|_|   
#                  _    
#     __ _ _ _  __| |                       
#    / _` | ' \/ _` |                       
#    \__,_|_||_\__,_|                       
#     _____                      _ _  _ _   
#    |_   _|____ ___  _ __ _ _ _| | |(_) |__
#      | |/ _ \ \ / || / _` | '_|_  _| | / /
#      |_|\___/_\_\\_, \__,_|_|   |_||_|_\_\
#                  |__/                     
#
#                 © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# scope: hikka_only
# meta developer: @AstroModules
# meta pic: https://img.icons8.com/clouds/500/000000/lock-2.png
# meta banner: https://0x0.st/oQgL.jpg

import random
from .. import loader, utils
from telethon.tl.types import Message
import asyncio
@loader.tds
class RandomGeneratePasswordMod(loader.Module):
    """🇷🇺 Генератор рандомного пароля/пин-кода
    Настроить генератор можно через конфиг
    Авторы: @Den4ikSuperOstryyPer4ik и @ToXicUse
    🇺🇸 Random password/pincode generator
    You can configure the generator through the config
    Authors: @Den4ikSuperOstryyPer4ik и @ToXicUse"""

    strings = {
        "name": "RandomPasswordGenerator",
        "_cfg_doc_pass_length": "set password length (in number of characters)",
        "_cfg_doc_pin_code_length": "set pincode length (in number of characters)",
        "_cfg_doc_simbols_in_pass": "Will there be additional characters in the generated password (+-*!&$#?=@<>)?",
        "what_to_generate": "What should be generated?",
        "new_random_pass": "new random password",
        "new_random_pincode": "new random pincode",
    }
    strings_ru = {
        "_cfg_doc_pass_length": "выставьте длину пароля(в кол-ве символов)",
        "_cfg_doc_pin_code_length": "выставьте длину Пин-Кода(в кол-ве символов)",
        "_cfg_doc_simbols_in_pass": "Какие символы должны быть в сгенерированном пароле?",
        "what_to_generate": "Что надо сгенерировать?",
        "_cmd_doc_generatorcfg": "—>конфиг этого модуля",
        "_cmd_doc_igenerator": "—>сгенерировать случайный пароль/пин-код",
        "new_random_pass": "новый рандомный пароль",
        "new_random_pincode": "новый рандомный пин-код",
    }

    async def generatorcfgcmd(self, message: Message):
        """—>config for this module"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "password_length",
                10,
                doc=lambda: self.strings("_cfg_doc_pass_length"),
                validator=loader.validators.Integer(minimum=8),
            ),
            loader.ConfigValue(
                "pincode_length",
                4,
                doc=lambda: self.strings("_cfg_doc_pin_code_length"),
                validator=loader.validators.Integer(minimum=4),
            ),
            loader.ConfigValue(
                "symbols_in_pass",
                "+-*!&$?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                doc=lambda: self.strings("_cfg_doc_simbols_in_pass"),
            )
        )
    async def igeneratorcmd(self, message: Message):
        """—>generate random password/pin"""
        await self.inline.form(
            self.strings("what_to_generate"),
            reply_markup=[
                [
                    {
                        "text": self.strings("new_random_pass"),
                        "callback": self.new_random_pass
                    },
                ],
                [
                    {
                        "text": self.strings("new_random_pincode"),
                        "callback": self.new_random_pincode
                    },
                ],
                [
                    {
                        "text": "🚫 Close | 🚫 Закрыть",
                        "action": "close",
                    },
                ],
            ],
            message=message,
        )
    async def new_random_pass(self, message: Message):
        symbols_in_pass = self.config["symbols_in_pass"]
        password_length = self.config["password_length"]
        await utils.answer(message, f'<em>Ваш новый случайный пароль в {password_length} символов генерируется...| Your new random password in {password_length} characters is being generated...</em>')
        await asyncio.sleep(1)
        length = int(self.config["password_length"])
        password = ''
        for i in range(length):
            password += random.choice(symbols_in_pass)
            await utils.answer(message, f'<b>Ваш новый сгенерированный пароль в {password_length} символов: <code>{password}</code> | Your new generated password in {password_length} characters: <code>{password}</code></b>')
    async def new_random_pincode(self, message: Message):
        pincode_length = self.config["pincode_length"]
        await utils.answer(message, f'<em>Ваш новый случайный пин-код в {pincode_length} символов генерируется... | Your new random pincode in {pincode_length} characters is being generated...</em>')
        await asyncio.sleep(1)
        chars = '1234567890'
        length = int(self.config["pincode_length"])
        pincode = ''
        for i in range(length):
            pincode += random.choice(chars)
            await utils.answer(message, f'<b>Ваш новый сгенерированный пин-код в {pincode_length} символов:</b> <code>{pincode}</code>')
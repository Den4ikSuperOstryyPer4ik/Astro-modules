#               _             __  __           _       _           
#     /\       | |           |  \/  |         | |     | |          
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___ 
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#                © Copyright 2022

#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse

#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
# scope: hikka_only
# meta developer: @AstroModules
# meta pic: https://img.icons8.com/clouds/500/000000/lock-2.png
# meta banner: https://i.imgur.com/rJScJY9.jpeg
# scope: inline
# scope: hikka_min 1.3.0
__version__ = (2, 0, 0)
from .. import loader, utils
from telethon.tl.types import Message
import logging, random
from ..inline.types import InlineCall
logger = logging.getLogger(__name__)
@loader.tds
class PasswordGeneratorMod(loader.Module):
    """
    Random password/pincode generator
    You can configure the generator through the config
    """

    strings = {
        "name": "RandomPasswordGenerator",
        "_cfg_doc_pass_length": "set password length (in number of characters)",
        "_cfg_doc_pin_code_length": "set pincode length (in number of characters)",
        "_cfg_doc_simbols_in_pass": "Will there be additional characters in the generated password (+-*!&$#?=@<>)?",
        "what_to_generate": "🆗What should be generated?",
        "new_random_pass": "🔣 new random password 🆕",
        "new_random_pincode": "🔢 new random PIN-code 🆕",
        "pass": "<b>🆕 Your new password in {} characters:\n<code>{}</code></b>",
        "pincode": "<b>🆕 Your new pincode in {} characters:\n<code>{}</code></b>", 
        "menu": "💻 Menu",
        "close": "🚫 Close"
    }

    strings_ru = {
        "_cls_doc": "Генератор рандомного пароля/пин-кода\nНастроить генератор можно через конфиг",
        "_cfg_doc_pass_length": "выставьте длину пароля(в кол-ве символов)",
        "_cfg_doc_pin_code_length": "выставьте длину Пин-Кода(в кол-ве символов)",
        "_cfg_doc_simbols_in_pass": "Какие символы должны быть в сгенерированном пароле?",
        "what_to_generate": "🆗 Что надо сгенерировать?",
        "new_random_pass": "🔣 Новый рандомный пароль 🆕",
        "new_random_pincode": "🔢 Новый рандомный PIN-код 🆕",
        "pass": "<b>🆕 Ваш новый пароль в {} символов:\n<code>{}</code></b>",
        "pincode": "<b>🆕 Ваш новый пин-код в {} символов:</b>\n<code>{}</code>",
        "menu": "💻 Меню",
        "close": "🚫 Закрыть",
    }

    async def client_ready(self, client, db):
        logger.info("Привет от t.me/AstroModules :)")

    @loader.command(ru_doc="—>конфиг этого модуля")
    async def generatorcfgcmd(self, message: Message):
        """—>config for this module"""
        name = self.strings("name")
        await self.allmodules.commands["config"](await utils.answer(message, f"{self.get_prefix()}config {name}"))

    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "password_length",
                10,
                doc=lambda: self.strings("_cfg_doc_pass_length"),
                validator=loader.validators.Integer(minimum=6),
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

    @loader.command(ru_doc="—>сгенерировать случайный пароль/пин-код")
    async def igeneratorcmd(self, message: Message):
        """—>generate random password/pin"""
        await self.inline.form(
            self.strings("what_to_generate"),
            reply_markup=[
                [{"text": self.strings("new_random_pass"), "callback": self.new_random_pass}],
                [{"text": self.strings("new_random_pincode"), "callback": self.new_random_pincode}],
                [{"text": self.strings("close"), "action": "close"}],
            ],
            message=message,
        )

    async def igenerator(self, call: InlineCall):
        await call.edit(
            self.strings("what_to_generate"),
            reply_markup=[
                [{"text": self.strings("new_random_pass"), "callback": self.new_random_pass}],
                [{"text": self.strings("new_random_pincode"), "callback": self.new_random_pincode}],
                [{"text": self.strings("close"), "action": "close"}],
            ],
        )

    async def new_random_pass(self, call: InlineCall):
        symbols_in_pass = self.config["symbols_in_pass"]
        password_length = self.config["password_length"]
        length = int(password_length)
        password = ''
        for i in range(length):
            password += random.choice(symbols_in_pass)
            await call.edit(
                self.strings["pass"].format(password_length, password),
                reply_markup=[
                [{"text": self.strings("menu"), "callback": self.igenerator}],
                [{"text": self.strings("close"), "action": "close"}]
                ]
            )

    async def new_random_pincode(self, call: InlineCall):
        pincode_length = self.config["pincode_length"]
        chars = '1234567890'
        length = int(self.config["pincode_length"])
        pincode = ''
        for i in range(length):
            pincode += random.choice(chars)
            await call.edit(
                self.strings["pincode"].format(pincode_length, pincode),
                reply_markup=[
                [{"text": self.strings("menu"), "callback": self.igenerator}],
                [{"text": self.strings("close"), "action": "close"}]
                ]
            )
__version__ = (1, 0, 0)
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/Achievements.jpg
# meta developer: @AstroModules
# requires: pillow

import base64
import io
import os
import re
from typing import Union

import requests
from hikkatl.tl.types import MessageMediaDocument, MessageMediaPhoto
from PIL import Image

from .. import loader, utils

MIME_TYPES = ["webp", "png", "jpeg", "jpg", "bmp", "dds", "dib", "eps", "ico", "tiff"]


def is_hex_color(value: str):
    return True if re.match(r'^#(?:[0-9a-fA-F]{1,2}){3}$', value) else False


class HexColorValidator(loader.validators.Validator):
    """#HexColor Validator"""

    def __init__(self):
        super().__init__(
            self._validate,
            {
                "en": "hex color in format #RRGGBB",
                "ru": "цвет в формате #RRGGBB"
            }
        )

    @staticmethod
    def _validate(value) -> str:
        if not isinstance(value, str):
            raise loader.validators.ValidationError("Value must be a string - valid hex color in format #RRGGBB")
        
        try:
            if not is_hex_color(value):
                raise Exception()
        except Exception:
            raise loader.validators.ValidationError(f"Passed value ({value}) is not a valid hex color in format #RRGGBB")

        return value


class AchievementsMod(loader.Module):
    """Create the achievement from https://minecraft-inside.ru/achievements/
    
    Idea from @Den4ikSOP & @boyhao
    """
    
    strings = {
        "name": "Achievements",
        "text_color_cfg": "Text color in format #RRGGBB (hex, default #ffffff)",
        "title_color_cfg": "Title color in format #RRGGBB (hex, default #ffff00)",
        "icon_id_cfg": "Icon ID (1-1099, default 893) from https://minecraft-inside.ru/achievements/ (row number * 15 + icon number in row from 1 to 15)",
        "invalid_length": "🚫 The length of the text must be between 1 and 45 characters",
        "invalid_icon_id": "🚫 The icon ID must be between 1 and 1099",
        "invalid_color": "🚫 The color must be in the format #RRGGBB",
        "title_cfg": "Title of achievement (no more than 45 characters)",
    }

    strings_ru = {
        "_cls_doc": "Создает достижение из https://minecraft-inside.ru/achievements/\n\nIdea from @Den4ikSOP & @boyhao",
        "text_color_cfg": "Цвет текста в формате #RRGGBB (hex, по умолчанию #ffffff)",
        "title_color_cfg": "Цвет заголовка в формате #RRGGBB (hex, по умолчанию #ffff00)",
        "icon_id_cfg": "ID иконки (от 1 до 1099) из https://minecraft-inside.ru/achievements/ (номер строки * 15 + номер иконки в строке от 1 до 15)",
        "invalid_length": "🚫 Длина текста должна быть между 1 и 45 символами",
        "invalid_icon_id": "🚫 ID иконки должен быть между 1 и 1099",
        "invalid_color": "🚫 Цвет должен быть в формате #RRGGBB",
        "title_cfg": "Заголовок достижения (не более 45 символов)",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "text_color",
                "#ffffff",
                lambda: self.strings("text_color_cfg"),
                validator=HexColorValidator(),
            ),
            loader.ConfigValue(
                "title_color",
                "#ffff00",
                lambda: self.strings("title_color_cfg"),
                validator=HexColorValidator(),
            ),
            loader.ConfigValue(
                "icon_id",
                893,
                lambda: self.strings("icon_id_cfg"),
                validator=loader.validators.Integer(minimum=1, maximum=1099),
            ),
            loader.ConfigValue(
                "title",
                "Новое достижение!",
                lambda: self.strings("title_cfg"),
                validator=loader.validators.String(min_len=1, max_len=45),
            )
        )

    async def download_media(self, message):
        media = None
        msg = None
        if message.media:
            media, msg = message.media, message
        elif (reply := await message.get_reply_message()) and reply.media:
            media, msg = reply.media, reply

        if not (media and msg) or getattr(msg, "sticker") or not isinstance(media, (MessageMediaDocument, MessageMediaPhoto)):
            return False

        
        if (isinstance(media, MessageMediaDocument) and media.document) and (not (image := re.match(r"image/(.*)", media.document.mime_type)) or image.group(1) not in MIME_TYPES):
            return False

        return await msg.download_media()

    def generateAchievement(
            self,
            title: str,
            text: str,
            icon: Union[str, bytes, io.BytesIO],
            title_color: str,
            text_color: str,
            file_mime_type: str = "png"
    ):
        if len(text) > 45 or len(title) > 45:
            raise ValueError(self.strings("invalid_length"))
        
        if isinstance(icon, str) and icon.isdigit() or isinstance(icon, int):
            data_icon = f"i{icon}"
        elif isinstance(icon, (bytes, io.BytesIO)):
            if isinstance(icon, io.BytesIO):
                icon = icon.getvalue()
            data_icon = f"data:image/{file_mime_type};base64,{base64.b64encode(icon).decode()}"
            
        return requests.post(
            "https://den4iksop.org/tg-stickers-api/achievement",
            json={
                "title": title,
                "text": text,
                "data_icon": data_icon,
                "title_color": title_color,
                "text_color": text_color
            }
        )

    async def create_achievement(self, message):
        args: list[str] = utils.get_args(message)

        title_color = self.config["title_color"]
        text_color = self.config["text_color"]
        icon = self.config["icon_id"]
        for arg in args.copy():
            if arg == "-icon":
                icon = args[args.index(arg) + 1]
                if not icon.isdigit() or not 0 < int(icon) < 1099:
                    raise ValueError(self.strings("invalid_icon_id"))
                args.pop(args.index(icon))
            elif arg == "-text-color":
                text_color = args[args.index(arg) + 1]
                if not is_hex_color(text_color):
                    raise ValueError(self.strings("invalid_color"))
                args.pop(args.index(text_color))
            elif arg == "-title-color":
                title_color = args[args.index(arg) + 1]
                if not is_hex_color(title_color):
                    raise ValueError(self.strings("invalid_color"))
                args.pop(args.index(title_color))
            else:
                continue

            args.pop(args.index(arg))

        file_name = await self.download_media(message)
        if file_name:
            image = Image.open(file_name)
            resized_image = image.resize((32, 32))

            file = io.BytesIO()
            resized_image.save(file, format="PNG")
            file.seek(0)

        count = len(args)
        achievement_response = await utils.run_sync(
            self.generateAchievement,
            title=args[0] if count == 2 else self.config["title"],
            text=args[1] if count == 2 else args[0],
            icon=file if file_name else icon,
            title_color=title_color,
            text_color=text_color
        )
        if file_name:
            os.remove(file_name)

        b64file = achievement_response.json()["image"][22:]
        return base64.b64decode(b64file)


    @loader.command(
        ru_doc="[Заголовок] \"<текст>\" [-icon <id>] [-title-color #<цвет>] [-text-color #<цвет>]",
        alias="ach",
    )
    async def achievement(self, message):
        """[title] \"<text>\" [-icon <id>] [-title-color #<color>] [-text-color #<color>]"""
        try:
            sticker_file = await self.create_achievement(message)
        except ValueError as e:
            await utils.answer(message, str(e))
            return
        
        sticker = await self.client.upload_file(sticker_file)
        sticker.name = "achievement.webp"

        if not (msg := await message.get_reply_message()):
            msg = message
        
        await utils.answer_file(message, sticker, reply_to=msg)

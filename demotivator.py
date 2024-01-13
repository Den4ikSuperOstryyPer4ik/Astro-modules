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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/Demotivator.jpg
# requires: pillow

import io
import os
import re
from typing import Optional

import requests
from hikkatl.tl.types import MessageMediaDocument, MessageMediaPhoto
from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps

from .. import loader, utils

MIME_TYPES = ["webp", "png", "jpeg", "jpg", "bmp", "dds", "dib", "eps", "ico", "tiff"]


class FontValidator(loader.validators.Validator):
    """Valid link to file with font"""

    def __init__(self):
        super().__init__(
            self._validate,
            {
                "en": "link to file with font",
                "ru": "ссылкой на файл со шрифтом"
            }
        )

    @staticmethod
    def _validate(value) -> str:
        if not isinstance(value, str):
            raise loader.validators.ValidationError("Value must be a string - URL(Link) to file with font.")
        
        try:
            if not value.endswith(".ttf") or not utils.check_url(value):
                raise Exception("Invalid URL")
        except Exception:
            raise loader.validators.ValidationError(f"Passed value ({value}) is not a valid URL to file with font.")

        return value


class ColorValidator(loader.validators.Validator):
    """Valid string color (for PIL.ImageColor)"""

    def __init__(self):
        super().__init__(
            self._validate,
            {
                "en": "color (red/blue/green/...)",
                "ru": "цветом (red/blue/green/...)",
            }
        )

    @staticmethod
    def _validate(value) -> str:
        if not isinstance(value, str):
            raise loader.validators.ValidationError("Value must be a string - valid color")

        try:
            _ = ImageColor.getcolor(value, "RGBA")
        except Exception:
            raise loader.validators.ValidationError(f"Passed value ({value}) is not a valid color")

        return value


@loader.tds
class DemotivatorMod(loader.Module):
    '''Demotivate picture with text, arguments and config.'''

    strings = {
        "name": "Demotivator",
        "require_photo": "<b>Reply with a photo, attach it to the team.</b>",
        "require_text": "<b>Text required!</b>",
        "require_args": "<b>Args required!</b>",
        "error": "<b>An error occurred...</b>",
        "success": "<b>Result:</b>",
        "demotivation": "<b>Demotivation, please wait...</b>",
        "watermark_cfg": "Default watermark.",
        "font_color_cfg": "Default text font color.",
        "fill_color_cfg": "Default background color",
        "font_name_cfg": "Link to font file (.ttf, not .zip)",
        "top_size_cfg": "Default top text size.",
        "bottom_size_cfg": "Default additional (bottom) text size.",
        "arrange_cfg": "Adjust photo frames or not",
    }

    strings_ru = {
        "require_photo": "<b>Ответьте на фото, приложите его к команде.</b>",
        "require_text": "<b>Необходим текст!</b>",
        "require_args": "<b>Необходимы аргументы!</b>",
        "error": "<b>Произошла ошибка...</b>",
        "success": "<b>Результат:</b>",
        "demotivation": "<b>Демотивация, подождите, пожалуйста...</b>",
        "watermark_cfg": "Водяной знак по умолчанию.",
        "font_color_cfg": "Цвет шрифта текста по умолчанию.",
        "fill_color_cfg": "Цвет фона по умолчанию",
        "font_name_cfg": "Ссылка на файл со шрифтом (.ttf, не .zip)",
        "top_size_cfg": "Размер главного текста по умолчанию.",
        "bottom_size_cfg": "Размер дополнительного (нижнего) текста по умолчанию.",
        "arrange_cfg": "Регулировать рамки под фотографию или нет",
        "_cls_doc": "Демотивировает картинку по параметрам(текст, аргументы и конфиг)."
    }

    def __init__(self) -> None:
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "watermark",
                "@AstroModules",
                lambda: self.strings("watermark_cfg"),
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "font_color",
                "white",
                lambda: self.strings("font_color_cfg"),
                validator=ColorValidator(),
            ),
            loader.ConfigValue(
                "fill_color",
                "black",
                lambda: self.strings("fill_color_cfg"),
                validator=ColorValidator(),
            ),
            loader.ConfigValue(
                "font_name_link",
                "https://0x0.st/HHyo.ttf",
                lambda: self.strings("font_name_cfg"),
                validator=FontValidator(),
            ),
            loader.ConfigValue(
                "top_size",
                80,
                lambda: self.strings("top_size_cfg"),
                validator=loader.validators.Integer(minimum=10),
            ),
            loader.ConfigValue(
                "bottom_size",
                60,
                lambda: self.strings("bottom_size_cfg"),
                validator=loader.validators.Integer(minimum=10),
            ),
            loader.ConfigValue(
                "arrange",
                True,
                lambda: self.strings("arrange_cfg"),
                validator=loader.validators.Boolean(),
            ),
        )


    def parse_args(self, text: str):
        args = text.replace("\n", " ").split(" ")
        text = " " + text
        parsed = {}

        for arg in args:
            try:
                if arg in ["-bottom-text", "-btm-text", "-bottom"]:
                    parsed["bottom_text"] = args[args.index(arg)+1]
                elif arg in ["-wt", "-watermark"]:
                    parsed["watermark"] = args[args.index(arg)+1]
                elif arg in ["-font-color", "-ftc"]:
                    parsed["font_color"] = args[args.index(arg)+1]
                elif arg in ["-fill-color", "-flc"]:
                    parsed["fill_color"] = args[args.index(arg)+1]
                elif arg in ["-font-name", "-font", "-font-link"]:
                    parsed["font_name"] = args[args.index(arg)+1]
                elif arg in ["-top-size", "-tpsz", "-topsize"]:
                    parsed["top_size"] = args[args.index(arg)+1]
                elif arg in ["-bottom-size", "-btmsz"]:
                    parsed["bottom_size"] = args[args.index(arg)+1]
                elif arg in ["-arrange", "-arr"]:
                    parsed["arrange"] = True
                    text = text.replace(f" {arg}", "")
                    continue
                else:
                    continue

                text = text.replace(f" {arg} {args[args.index(arg)+1]}", "")
            except IndexError:
                pass

        parsed["top_text"] = text

        return parsed


    async def download_media(self, message):
        media = None
        msg = None
        if message.media:
            media, msg = message.media, message
        elif (reply := await message.get_reply_message()) and reply.media:
            media, msg = reply.media, reply

        if not (media and msg) or not isinstance(media, (MessageMediaDocument, MessageMediaPhoto)):
            return False

        if (isinstance(media, MessageMediaDocument) and media.document) and (not (image := re.match(r"image/(.*)", media.document.mime_type)) or image.group(1) not in MIME_TYPES):
            return False

        return await msg.download_media()


    def create_demot(self,
        top_text: str = "",
        bottom_text: str = "",
        *,
        file: str,
        watermark: Optional[str] = None,
        result_filename: str,
        font_color: str = 'white',
        fill_color: str = 'black',
        font_name,
        top_size: int = 80,
        bottom_size: int = 60,
        arrange: bool = False
    ):
        """
        This method in https://github.com/Infqq/simpledemotivators/blob/main/simpledemotivators/Demotivator.py
        Author: Infqq
        GitHub Repo: https://github.com/Infqq/simpledemotivators/
        """
        
        if arrange:
            user_img = Image.open(file).convert("RGBA")
            (width, height) = user_img.size
            img = Image.new('RGB', (width + 250, height + 260), color=fill_color)
            img_border = Image.new('RGB', (width + 10, height + 10), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)
        else:
            img = Image.new('RGB', (1280, 1024), color=fill_color)
            img_border = Image.new('RGB', (1060, 720), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            user_img = Image.open(file).convert("RGBA").resize((1050, 710))
            (width, height) = user_img.size
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)

        font_1 = ImageFont.truetype(font=font_name(), size=top_size, encoding='UTF-8')
        text_width = font_1.getsize(top_text)[0]

        while text_width >= (width + 250) - 20:
            font_1 = ImageFont.truetype(font=font_name(), size=top_size, encoding='UTF-8')
            text_width = font_1.getsize(top_text)[0]
            top_size -= 1

        font_2 = ImageFont.truetype(font=font_name(), size=bottom_size, encoding='UTF-8')
        text_width = font_2.getsize(bottom_text)[0]

        while text_width >= (width + 250) - 20:
            font_2 = ImageFont.truetype(font=font_name(), size=bottom_size, encoding='UTF-8')
            text_width = font_2.getsize(bottom_text)[0]
            bottom_size -= 1

        size_1 = drawer.textsize(top_text, font=font_1)
        size_2 = drawer.textsize(bottom_text, font=font_2)

        if arrange:
            drawer.text((((width + 250) - size_1[0]) / 2, ((height + 190) - size_1[1])), top_text, fill=font_color, font=font_1)
            drawer.text((((width + 250) - size_2[0]) / 2, ((height + 235) - size_2[1])), bottom_text, fill=font_color, font=font_2)
        else:
            drawer.text(((1280 - size_1[0]) / 2, 840), top_text, fill=font_color, font=font_1)
            drawer.text(((1280 - size_2[0]) / 2, 930), bottom_text, fill=font_color, font=font_2)

        if watermark:
            (width, height) = img.size
            idraw = ImageDraw.Draw(img)

            idraw.line((1000 - len(watermark) * 5, 817, 1008 + len(watermark) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=font_name(), size=20, encoding='UTF-8')
            size_2 = idraw.textsize(watermark.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])),
                       watermark.lower(), font=font_2)

        img.save(result_filename)
        os.remove(file)

        return result_filename
    
    
    async def demotivate_pic(self, args: dict):
        result_path = "/tmp/_demoted_" + args["file"]
        
        font_name = args.get("font_name", self.config["font_name_link"])
        font_resp = await utils.run_sync(requests.get, font_name)
        
        def _get_font():
            font = io.BytesIO(font_resp.content)
            font.name = font_name.split("/")[-1]
            return font
        
        result = self.create_demot(
            top_text=args["top_text"],
            bottom_text=args.get("bottom_text", ''),
            file=args["file"],
            watermark=args.get("watermark", self.config["watermark"]) if not args.get("arrange", self.config["arrange"]) else None,
            result_filename=result_path,
            font_color=args.get("font_color", self.config["font_color"]),
            font_name=_get_font,
            fill_color=args.get("fill_color", self.config["fill_color"]),
            top_size=int(args.get("top_size", self.config["top_size"])),
            bottom_size=int(args.get("bottom_size", self.config["bottom_size"])),
            arrange=args.get("arrange", self.config["arrange"]),
        )
        return result_path if result else ""


    @loader.command(
        ru_doc="""<текст>
        [-bottom/-btm-text/-bottom-text <текст> - доп. текст внизу]
        [-wt/-watermark <текст> - добавить водяной знак]
        [-font-color/-ftc <цвет> (red/while/blue/yellow/...) - цвет шрифта (по дефолту white)]
        [-fill-color/-flc <цвет> (red/while/blue/yellow/...) - цвет заднего фона (по дефолту black)]
        [-font/-font-name/-font-link <ссылка на файл со шрифтами> (не zip, а ttf) - шрифт для текста]
        [-top-size/-topsize/-tpsz <размер> (по дефолту 80) - размер главного текста]
        [-bottom-size/-btmsz <размер> (по дефолту 60) - размер доп.(нижнего) текста]
        [-arrange - регулировать рамки под фотографию]
        - демотивировать картинку по заданному тексту и аргументам
        """,
        alias="demot",
    )
    async def demotivate(self, message):
        """<text>
        [-bottom/-btm-text/-bottom-text <text> - add. text below]
        [-wt/-watermark <text> - add watermark]
        [-font-color/-ftc <color> (red/while/blue/yellow/...) - font color (white by default)]
        [-fill-color/-flc <color> (red/while/blue/yellow/...) - background color (black by default)]
        [-font/-font-name/-font-link <link to file with fonts> (not zip, but ttf) - font for text]
        [-top-size/-topsize/-tpsz <size> (default 80) - main text size]
        [-bottom-size/-btmsz <size> (default 60) - extra size text]
        [-arrange - adjust photo frames]
        - demotivate a picture according to the given text and arguments
        """
        if not (args := utils.get_args_raw(message)):
            return await utils.answer(message, self.strings("require_args"))

        m = await utils.answer(message, self.strings("demotivation"))
        
        args = self.parse_args(args)
        media = ''
        if not args:
            return await utils.answer(m, self.strings("require_args"))
        elif not args.get("top_text", None):
            return await utils.answer(m, self.strings("require_text"))
        
        if not (media := await self.download_media(message)):
            return await utils.answer(m, self.strings("require_photo"))
        
        args["file"] = media

        demoted = await self.demotivate_pic(args)
        if not demoted:
            return await utils.answer(m, self.strings("error"))

        await utils.answer_file(m, demoted, self.strings("success"), reply_to=(await message.get_reply_message()))
        os.remove(demoted)

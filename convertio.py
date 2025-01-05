__version__ = (1, 0, 0)

import asyncio
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/Convertio.jpg
# meta developer: @AstroModules

import base64
import os

import requests

from .. import loader, utils


async def download_media(message):
    media = None
    msg = None
    if message.media:
        media, msg = message.media, message
    elif (reply := await message.get_reply_message()) and reply.media:
        media, msg = reply.media, reply

    if not (media and msg):
        return False

    return await msg.download_media()


def generate_api_key():
    return requests.post("https://den4iksop.org/convertio/getApiKey").json()


class ConvertioClient:
    # Original from https://github.com/PetitPotiron/python-convertio/blob/main/convertio/client.py#L14
    # This is edited version

    def __init__(self, token: str) -> None:
        self.token = token

    def upload(self, fp: str, output_format: str):
        """Converts the file found in the path provided.

        Args:
            fp (str): The file's path
            output_format (str): The file format you want the file to be converted to
        """
        r1 = requests.post(
            "http://api.convertio.co/convert",
            json={
                "apikey": self.token,
                "input": "upload",
                "outputformat": output_format,
            }
        ).json()
        if r1.get("error", None):
            raise ValueError(r1["error"])
        id = r1['data']['id']

        with open(fp, 'rb') as file:
            content = file.read()

        r2 = requests.put(f'http://api.convertio.co/convert/{id}/{fp.split("/")[-1]}', data=content).json()
        if r2.get("error", None):
            raise ValueError(r2["error"])

        return id

    def check_conversion(self, id: str):
        """Checks the step of a conversion

        Args:
            id (str) : The id of the conversion

        Returns:
            Conversion: The status of the conversion
        """
        r = requests.get(f"https://api.convertio.co/convert/{id}/status").json()
        if r.get("error", None):
            raise ValueError(r["error"])

        return {
            "code": r['code'],
            "status": r['status'],
            "id": r['data']['id'],
            "step": r['data']['step'],
            "step_percent": r['data']['step_percent'],
            "minutes": r['data']['minutes'],
        }

    def download(self, id: str, fp: str) -> None:
        """Writes the file content to a path."""
        r = requests.get(f"https://api.convertio.co/convert/{id}/dl").json()
        if r.get("error", None):
            raise ValueError(r["error"])

        if r['status'] == 'error':
            raise ValueError(r['error'])

        content = base64.b64decode(r["data"]["content"])

        with open(fp, "wb") as file:
            file.write(content)

        return fp


class ConvertioMod(loader.Module):
    """Convert file with api from https://convertio.co"""

    strings = {
        "name": "Convertio",
        "converting": "<emoji document_id=5440739140347907722>☺️</emoji><b> Wait, converting...</b>",
        "getting_api_key": "<emoji document_id=5220033539944237102>#️⃣</emoji><b> Wait, getting random API key...</b>",
        "error": "<emoji document_id=5213157963023273778>💔</emoji><b> Something went wrong...</b>\n<emoji document_id=5220115526574950412>💭</emoji> Contact @AstroModsChat",
        "no_file": "<emoji document_id=5219866512961062330>⁉️</emoji> <b>Where is the file?</b>",
        "no_args": "<emoji document_id=5206479194388713063>❓</emoji> <b>Where is the file format you want to convert the file to?</b>",
        "renewed": "<emoji document_id=5199658498559854923>🍀</emoji> <b>New API-key generated and saved!</b>",
        "downloading_file": "<emoji document_id=5217697679030637222>⏳</emoji> <b>Downloading your file...</b>",
        "converted": "<emoji document_id=5220064167356025824>⭐️</emoji> <b>File successfully converted from</b> <code>{}</code> to <code>{}</code>",
        "api_error": "<emoji document_id=5220214598585568818>🚨</emoji><b> API:</b> <i>{}</i>",
        "uploading": "<emoji document_id=5440739140347907722>☺️</emoji> <b>File converted. Uploading to Telegram...</b>",
    }

    strings_ru = {
        "_cls_doc": "Конвертирует файл с помощью https://convertio.co",
        "converting": "<emoji document_id=5440739140347907722>☺️</emoji><b> Подождите, идёт конвертация...</b>",
        "getting_api_key": "<emoji document_id=5220033539944237102>#️⃣</emoji><b> Подождите, получаю рандомный API KEY...</b>",
        "error": "<emoji document_id=5213157963023273778>💔</emoji><b> Что-то пошло не так...</b>\n<emoji document_id=5220115526574950412>💭</emoji> Обратитесь в @AstroModsChat",
        "no_file": "<emoji document_id=5219866512961062330>⁉️</emoji> <b>Где файл?</b>",
        "no_args": "<emoji document_id=5206479194388713063>❓</emoji> <b>Где формат файла, в который вы хотите преобразовать файл?</b>",
        "renewed": "<emoji document_id=5199658498559854923>🍀</emoji> <b>Новый API-ключ сохранен!</b>",
        "downloading_file": "<emoji document_id=5217697679030637222>⏳</emoji> <b>Загружаю ваш файл...</b>",
        "converted": "<emoji document_id=5220064167356025824>⭐️</emoji> <b>Файл успешно конвертирован с</b> <code>{}</code> в <code>{}</code>",
        "uploading": "<emoji document_id=5440739140347907722>☺️</emoji><b> Файл конвертирован. Загружаю в Telegram...</b>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "API_KEY",
                None,
                lambda: "API key from https://developers.convertio.co (Getting automatically)",
                validator=loader.validators.String()
            )
        )

    async def convert_file(self, message, m) -> str:
        args: str = utils.get_args_raw(message)
        if not args:
            raise ValueError(self.strings("no_args"))

        m = await utils.answer(m, self.strings("downloading_file"))
        file_name = await download_media(message)
        if not file_name:
            raise ValueError(self.strings("no_file"))

        m = await utils.answer(m, self.strings("converting"))
        client = ConvertioClient(token=self.config["API_KEY"])
        conversion_id = await utils.run_sync(client.upload, file_name, args)
        os.remove(file_name)

        while (await utils.run_sync(client.check_conversion, conversion_id))["step"] != 'finish':
            await asyncio.sleep(1)

        m = await utils.answer(m, self.strings("uploading"))
        output_file_path = os.path.abspath("".join([*file_name.split(".")[:-1], ".", args]))
        await utils.run_sync(client.download, conversion_id, output_file_path)

        return output_file_path, file_name.split(".")[-1], output_file_path.split(".")[-1], m

    @loader.command(alias="renewconv")
    async def renewconvertio(self, message):
        """Renew convertio api key"""
        await utils.answer(message, self.strings("getting_api_key"))
        response = await utils.run_sync(generate_api_key)
        if response["status"] == "Failed":
            await utils.answer(self.strings("error"))
            return

        self.config["API_KEY"] = response["api_key"]

        await utils.answer(message, self.strings("renewed"))

    @loader.command(
        ru_doc="<выходной формат> | Пример: png",
        alias="conv",
    )
    async def convert(self, message):
        """<output format> <!reply to file> | Example: png"""
        m = message

        if not self.config["API_KEY"]:
            m = await utils.answer(message, self.strings("getting_api_key"))
            response = await utils.run_sync(generate_api_key)
            if response["status"] == "Failed":
                await utils.answer(self.strings("error"))
                return

            self.config["API_KEY"] = response["api_key"]

        try:
            new_file, old_format, new_format, m = await self.convert_file(message, m)
        except ValueError as e:
            await utils.answer(m, self.strings("api_error").format(str(e)))
            return
        except Exception as e:
            await utils.answer(m, self.strings("error") + "\n\n" + utils.escape_html(str(e)))
            raise e

        if not (msg := await message.get_reply_message()):
            msg = message

        await utils.answer_file(
            m, new_file.split("/")[-1],
            reply_to=msg,
            caption=self.strings("converted").format(
                old_format.upper(), new_format.upper()
            ),
            force_document=True
        )
        os.remove(new_file.split("/")[-1])

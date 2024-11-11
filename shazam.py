__version__ = (1, 0, 0)
#   
#    @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
#   @@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
#   @@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
#   !@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
#   @!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
#   !!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
#   !!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
#   :!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
#   ::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
#    :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
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

# The code snippet is adapted from VoiceMod code by D4n1l3k300
# requires: ShazamAPI

import io
from ShazamAPI import Shazam
from .. import loader, utils

@loader.tds
class ShazamMod(loader.Module):
    """Use <reply to voice> to search for a song using audio."""

    strings = {
        "name": 'Shazam',
        "Downloading": "<emoji document_id=5971801057540443125>📥</emoji> <b>Downloading...</b>",
        "Searching": "<emoji document_id=5972211849687470465>🔎</emoji> <b>Searching...</b>",
        "no_reply": "<emoji document_id=5321004106494526877>🎤</emoji> <b>Please reply to an audio message.</b>",
        "not_found": "<emoji document_id=5346107391475725719>🤷‍♂️</emoji> <b>Song not found.</b>\n<i>Sorry..(</i>",
        "track_info": (
            "<emoji document_id=5346259862814734771>📱</emoji> <b>Song found! Title:</b>\n"
            "\n<emoji document_id=5879841310902324730>✏️</emoji> <code>{}</code>"
        )
    }

    strings_ru = {
        "Downloading": "<emoji document_id=5971801057540443125>📥</emoji> <b>Загрузка...</b>",
        "Searching": "<emoji document_id=5972211849687470465>🔎</emoji> <b>Поиск...</b>",
        "no_reply": "<emoji document_id=5321004106494526877>🎤</emoji> <b>Пожалуйста, ответьте на аудиосообщение.</b>",
        "not_found": "<emoji document_id=5346107391475725719>🤷‍♂️</emoji> <b>Не удалось найти песню.</b>\n<i>Извините хозяин..~</i>",
        "track_info": (
            "<emoji document_id=5346259862814734771>📱</emoji> <b>Песня найдена! Название:</b>\n"
            "\n<emoji document_id=5879841310902324730>✏️</emoji> <code>{}</code>"
        )
    }

    async def fetch_audio(self, message):
        reply = await message.get_reply_message()
        if reply and reply.file and reply.file.mime_type.startswith("audio"):
            await utils.answer(message, self.strings['Downloading'])
            audio_data = io.BytesIO(await reply.download_media(bytes))
            await utils.answer(message, self.strings['Searching'])
            return audio_data, reply
        await utils.answer(message, self.strings['no_reply'])
        return None, None

    @loader.command(ru_doc='<reply to audio> - распознать трек')
    async def sh(self, message):
        """<reply to audio> - recognize track"""
        audio_data, reply = await self.fetch_audio(message)
        if not audio_data:
            return

        try:
            shazam = Shazam(audio_data.read())
            recog = next(shazam.recognizeSong())[1]["track"]
            await self.client.send_file(
                message.peer_id,
                file=recog["images"]["background"],
                caption=self.strings['track_info'].format(recog["share"]["subject"]),
                reply_to=reply.id,
            )
            await message.delete()
        except Exception:
            await utils.answer(message, self.strings['not_found'])
